import os
def run():
    rp = input("Do you want to run programm(Calculator, oder, how to make a programm for Kriwi OS): ")
    if rp == "Calculator":
        os.system("py calc.plk")
    if rp == "oder":
	    pr = input("Name of your .plk Programm: ")
	    os.system("py " + pr + ".plk")
    if rp == "how to make a programm for Plekster OS":
        print("Make a python progaramm, change the extension of the file that launches the program to .plk")
        run()
def boot():
    print("Plekstr OS Loading...")
    print("Plekstr OS Load")
    import os
    run()
