from scriptcontext import doc
from services.log import debug


class ValueRepo:
    section = "ReTools"
    entry = ""
    default_value = None
    value_type = None

    def factory(self, value_string):
        pass

    def destructor(self, value):
        pass

    def get(self):
        debug("Repo: {}".format(".".join([self.section, self.entry])))
        debug("Value Type:{}".format(self.value_type))
        debug("Default value: {}".format(self.default_value))
        debug("Grabbing Value String")
        value_str = doc.Strings.GetValue(
            self.section,
            self.entry,
        )

        debug("Value string: {}".format(value_str))
        # Initialize value if necessary
        if value_str in ["", None]:
            debug("Initializing value repo")
            self.set(self.default_value)
            return self.default_value

        # Cast to value type using the value type constructor
        return self.factory(value_str)

    def set(self, value):
        # Destructure value
        str_value = self.destructor(value)

        # Set value
        doc.Strings.SetString(
            self.section,
            self.entry,
            str_value,
        )
