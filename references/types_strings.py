# This is a string
some_var = "Hello, world!"

# Strings are concatenated like this
a_long_string = "Hello, world!" + " " + "My name is Jamie."

# Strings can be 'formatted'
first_name = "Jamie"
last_name = "Phan"
job = "Software Engineer"

about_me_format = "Hello, world! My name is {:s} {:s} and I'm a {:s}"
about_me = about_me_format.format(
    first_name, last_name, job
)