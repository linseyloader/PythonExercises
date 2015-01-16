my_dict = {
    "Boston", "0 C"
    "Boise", "48 F"
    "Phoenix", "85 F"
    "Miami", "40 C"
    "Riverside", "30 C"
    "Baltimore", "32 F"
}

print sorted(my_dict, key=get_value)