from django.db import models

#multi select field that saves choices as bitfield
class MultipleChoiceField(models.Field):
    description = _("Encode multiple choices as bitmap")

    # Limit choices to width of integer in database
    def __init__(self, *args, **kwargs):
        self.disable_blank = kwargs.pop('disable_blank', False)
        kwargs['null'] = True
        kwargs['default'] = None
        if len(kwargs['choices']) > 32:
            raise ValueError(_("MultipleChoiceField does not support more than 32 choices."))
        for num, choices in kwargs['choices']:
            if num > 32:
                raise ValueError(_("MultipleChoiceField choices require numbers from 1 to 32"))
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['default']
        return name, path, args, kwargs

    # emulate integer field for schema selection
    def get_internal_type(self):
        return 'IntegerField'

    # decode integer to list of choices
    def decode_bitfield(self, value):
        selected = []
        for num, choice in self.choices:
            mask = 1 << num
            if value & mask:
                selected.append(num)
        return selected

    # encode list of choices into integer
    def encode_bitfield(self, value):
        if type(value) != list:
            raise ValueError(_("Choices must be a list."))
        ret = 0
        for num, choice in self.choices:
            mask = 1 << num
            if num in value:
                ret |= mask
        return ret

    # decode value from database to list
    def from_db_value(self, value, expression, connection):
        if value == None:
            return None
        return self.decode_bitfield(value)

    # deserialize model
    def to_python(self, value):
        if value == None:
            return None

        if isinstance(value, list):
            for v in value:
                if not v in [x for x, y in self.choices] and v != '':
                    raise ValidationError(_("Value %s is not a valid choice." % str(v)))
            return value

        # from form input
        if isinstance(value, str):
            # empty choices
            if value == '':
                return value

            # handle string casting to integer
            try:
                v = int(value)
            except ValueError as e:
                raise ValidationError(e)
            return v

        if isinstance(value, int):
            return self.decode_bitfield(value)

        raise ValidationError("Invalid type %s for MultipleChoiceField.")

    # encode choices to bitfield if possible
    def get_db_prep_value(self, value, connection, prepared=False):
        value = super().get_db_prep_value(value, connection, prepared)
        if value == None:
            return None
        if type(value) == int:
            return self.encode_bitfield([value])
        return self.encode_bitfield(value)

    # add custom get_field_display method
    def contribute_to_class(self, cls, name, private_only=False):
        super().contribute_to_class(cls, name, private_only)
        if self.choices:
            def get_display(obj):
                value = getattr(obj, name)
                choices = dict(self.choices)
                if value == None:
                    return None
                else:
                    return ', '.join([choices[x] for x in value])

            setattr(cls, 'get_%s_display' % self.name, get_display)

    # set form field for choice processing
    def formfield(self, **kwargs):
        defaults = {
            'choices_form_class': forms.TypedMultipleChoiceField,
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)

    # validate field input for forms
    def validate(self, value, model_instance):
        if not self.editable:
            return

        for v in value:
            if not v in [x for x, y in self.choices] and v not in '':
                raise ValidationError(_("Value %s is not a valid choice." % str(v)))
        return

    # allow disabling the empty choice for enhanced display
    def get_choices(self, *args, **kwargs):
        if self.disable_blank == True:
            kwargs['include_blank'] = False
        return super().get_choices(*args, **kwargs)
