from scriptcontext import doc


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
        # Grab value
        print("Repo: " + ".".join([self.section, self.entry]))
        print("Value Type: " + str(self.value_type))
        print("Default value: " + str(self.default_value))

        print("Grabbing Value String")
        value_str = doc.Strings.GetValue(
            self.section,
            self.entry,
        )

        print("Value string: " + str(value_str))
        # Initialize value if necessary
        if value_str in ["", None]:
            print("Initializing value repo")
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
