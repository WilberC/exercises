def is_valid_ip(strng: str):
    return (
            strng.count('.') == 3 and  # This valid the IP octets because it has to have 4 octets divided by 3 dots
            all(  # This reduces the array into a single True or False
                o.isdigit() and  # This takes approach of python function to valid if string is a number the
                # problem is that if you have a space or break line character it also counts it as a digit
                # so ' 1' or '1\n' will return true that's why we fix it with next line
                str(int(o)) == o and  # This is the icing on the cake, because it if we have ' 1\n' converted to int
                # we will have 1, but for IP this is wrong, so we convert it to string '1' and compare to the initial
                # input that should be '1' == ' 1\n' and that is False! With this we fix the isdigit() problem
                0 <= int(o) <= 255  # And here we just check the IP range of the octets
                for o in strng.split('.')
            )
    )
