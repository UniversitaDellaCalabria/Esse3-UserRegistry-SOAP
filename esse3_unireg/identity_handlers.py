EXAMPLE_DB = [
                dict(Name='Giuseppe',
                     Surname='De Marco',
                     CodiceFiscale='gdm17',
                     Email='gdm@unical.it',
                     Username='gdm',
                     Birthdate='2000-08-10',
                     Birthplace='',
                     Nationality='',
                     Sex='',
                     Passport=''),
                dict(Name='Francesco',
                     Surname='Filicetti',
                     CodiceFiscale='ciccio18',
                     Email='ciccio@unical.it',
                     Username='ciccio',
                     Birthdate='2000-08-10',
                     Birthplace='',
                     Nationality='',
                     Sex='',
                     Passport=''),
              ]


def identity_example(user_id):
    """ Example function that takes the uid and do a
        query to one or many data sources
    """
    for i in EXAMPLE_DB:
        # that's an OR approach with a first Match!
        if user_id.CodiceFiscale == i['CodiceFiscale'] or \
           user_id.Username == i['Username']:
            return i
