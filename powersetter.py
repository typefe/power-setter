import subprocess


def output_maker():
    itemList = []

    output = subprocess.check_output(["powercfg", "-list"])
    output_string = output.decode("ascii")
    output_string = "".join(output_string.split("\r\n"))
    output_string = output_string.split("Power Scheme GUID: ")
    output_string.pop(0)

    for i in output_string:
        i = i.split("  ")
        itemList.append(i)

    return itemList


def get_power_plans():
    print("""----------Power Options----------""")
    for index, (i, j) in enumerate(output):
        print(f"{index}-) {j},{i}")


def change_current_scheme_to_index(index):
    if index <= len(output) - 1:
        try:
            subprocess.call("powercfg /s {}".format(output[index][0]))
            print("Current scheme >>> {}".format(output[index][1]))
            return True
        except Exception as error:
            print(error)
            return False


try:
    output = output_maker()
except Exception as cantgetprocesserror:
    print(cantgetprocesserror)
