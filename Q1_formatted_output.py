# START
str11 = "Escape sequence"; str22 = "Description"
print(f"{str11:<20}{str22:>10}")

spaceline = str.format("%40s" % " ")
dashline = spaceline.replace(" ", "-")
print(dashline)

str1 = "\\"; str2 = "A single backslash"
print(f"{str1:<20}{str2:>15}")

str3 = "\\\\"; str4 = "A double backslash"
print(f"{str3:<20}{str4:>15}")

str5 = "''"; str6 = "A pair of single quotes"
print(f"{str5:<20}{str6:>15}")

str7 = "\"\""; str8 = "A pair of double quotes"
print(f"{str7:<20}{str8:>15}")