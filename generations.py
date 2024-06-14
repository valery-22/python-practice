print("Generation Identifier")
print()
year = int(input("Which year were you born?:"))
if year >= 1883 and year <= 1900:
    print("lost generation")
if year >= 1901 and year <= 1927:
    print("greatest generation")
    if year >= 1928 and year <= 1945:
        print("Silent generation")
        if year >= 1946 and year <= 1964:
            print("Baby boomers")
            if year >= 1965 and year <= 1980:
                print("Generation X")
                if year >= 1981 and year <= 1996:
                    print("Millenials")
                    if year >= 1997 and year <= 2012:
                        print("Generation Z")
                    else: 
                        print("Generaton Alpha")