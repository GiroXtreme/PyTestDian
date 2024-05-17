class List( type ):

    def __new__(type_ref, member_type):

        class List(list):

            def append(self, member):
                if not isinstance(member, member_type):
                    raise TypeError('Attempted to append a "{0}" to a "{1}" which only takes a "{2}"'.format(
                        type(member).__name__,
                        type(self).__name__,
                        member_type.__name__ 
                    ))

                    list.append(self, member)

        return List 