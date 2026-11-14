def main():
    camel_case_variable = input("Please input a variable name in camel case: ")
    print(to_camel_case(camel_case_variable))
#
def to_camel_case(s: str) -> str:
    result = ""

    for i in range(len(s)):
        char = s[i]
        if char.isupper():
            sub_result = char.lower()
            if i != 0:
                sub_result = "_" + sub_result

            result += sub_result
        else:
            result += char

    return result

assert "camel" == to_camel_case("camel")
assert "camel_case" == to_camel_case("camelCase")
assert "camel_case_case" == to_camel_case("camelCaseCase")
assert "camel_case_example" == to_camel_case("camelCaseExample")
assert "camel" == to_camel_case("Camel")
print("success")