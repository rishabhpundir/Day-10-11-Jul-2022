# STAR PATTERNS

# 1. RIGHT ANGLE TRIANGLE (LEFT LEAN)

# * 
# *  *
# *  *  *
# *  *  *  *
# *  *  *  *  *

# star = []

# for i in range(0, 5):
#     star.append('* ')
#     print(' '.join(star))


# -----------------------------------------------------------------------------------------


# 2. RIGHT ANGLE TRIANGLE (RIGHT LEAN)

#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# star = [' ', ' ', ' ', ' ', ' ']

# for i in range(0, 5):
#     star[len(star) -1 - i] = '*'
#     print(' '.join(star))


# -----------------------------------------------------------------------------------------


# 3. Triangle

#          * 
#        *   *
#      *   *   *
#    *   *   *   *
#  *   *   *   *   *

# star = [' ', ' ', ' ', ' ', ' ']

# for i in range(0, 5):
#     star[len(star) -1 - i] = ' * '
#     print(' '.join(star))


# -----------------------------------------------------------------------------------------


# # 4. A

#      *
#     * *
#    *   *
#   * * * *
#  *       *

# star = [' ', ' ', ' ', ' ', ' ']
# a = []
# for i in range(0, 5):
#     star[len(star) -1 - i] = ' *'
#     b = ''.join(star)
#     a.append(b)
    
# for i in range(0, len(a)):
#     if i < 2 or i==3:
#         print(a[i])
#     elif i == 2:
#         pattern = a[i].split()
#         for k in range(0, 3):
#             if 0 < k < 2:
#                 pattern[k] = ' '
#             new_pattern = ' '.join(pattern)
#         print('   ' + new_pattern)
#     elif i == 4:
#         pattern = a[i].split()
#         for k in range(0, 5):
#             if 0 < k < 4:
#                 pattern[k] = ' '
#             new_pattern = ' '.join(pattern)
#         print(' ' + new_pattern)


# -----------------------------------------------------------------------------------------


# # 4. B

# * * * *
# *       *
# * * * *
# *       *
# * * * *

# for i in range(0, 5):
#     star = ['*', '*', '*', '*', '*']
#     if i%2 == 0:
#         star.remove(star[-1])
#         print(' '.join(star))
#     elif i%2 != 0 and i != 0:
#         for j in range(0, len(star)):
#             if 0 < j < len(star)-1:
#                 star[j] = ' '
#         print(' '.join(star))


# -----------------------------------------------------------------------------------------


# # 5. C

#   * * * *
# *
# *
# *
#   * * * *

# for i in range(0, 5):
#     star = ['*', '*', '*', '*', '*']
#     if i%2 == 0 and i != 2:
#         for j in range(0, len(star)):
#             if j == 0:
#                 star[j] = ' '
#         print(' '.join(star))
#     elif i == 2:
#         for j in range(0, len(star)):
#             if 0 < j < len(star):
#                 star[j] = ' '
#         print(' '.join(star))
#     elif i%2 != 0:
#         for j in range(0, len(star)):
#             if 0 < j < len(star):
#                 star[j] = ' '
#         print(' '.join(star))


# -----------------------------------------------------------------------------------------


# # 5. D

# * * * *
# *       *
# *       *
# *       *
# * * * *

# for i in range(0, 5):
#     star = ['*', '*', '*', '*', '*']
#     if i%2 == 0 and i != 2:
#         star.remove(star[-1])
#         print(' '.join(star))
#     elif i%2 != 0 or i==2:
#         for j in range(0, 5):
#             if 0 < j < len(star)-1:
#                 star[j] = ' '
#         print(' '.join(star))


# -----------------------------------------------------------------------------------------


# Q. What are the Dunder/Magic/Special methods in Python?

# __init__

# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#         print(f'{self.fname} {self.lname}')

# human_obj = Person('Rishabh', 'Pundir')



# __repr__
# DEFAULT

# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

# human_obj = Person('Rishabh', 'Pundir')
# print(repr(human_obj))


#CUSTOMISED

# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

#     def __repr__(self):
#         return f'Person("{self.fname}", "{self.lname}")'

# human_obj = Person('Rishabh', 'Pundir')
# print(repr(human_obj))



# __str__

# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

#     def __repr__(self):
#         return f'Person("{self.fname}", "{self.lname}")'

#     def __str__(self):
#         return f'("{self.fname}", "{self.lname}")'


# human_obj = Person('Rishabh', 'Pundir')
# print(human_obj)
# print(repr(human_obj))


# -----------------------------------------------------------------------------------------


# Q. What is the most efficient way to concatenate many strings together?

# join()

# From the python docs:

    # Concatenating immutable sequences always results in a new object. This means that building up a sequence by repeated concatenation will have a quadratic runtime cost in the total sequence length.

# string = ['Mary', 'had', 'a', 'little', 'lamb.']
# print(' '.join(string))


# -----------------------------------------------------------------------------------------


# Q. What are Virtualenvs? Install package in virtual environment. How to create virtualenv and activate?

# Done


# -----------------------------------------------------------------------------------------


