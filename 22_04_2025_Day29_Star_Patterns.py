
# 5/5 square type stars
# *****
# *****
# *****
# *****
# *****

n=5
for i in range(n):
  print('*' *5)
#####################################
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

for i in range(n):
  for j in range(n):
    if i>= j:
      print('*', end =' ')
  print()

print("--------------------")

########################################

# * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(n):
  for j in range(n):
    if i<= j:
      print('*', end =' ')
  print()

print("--------------------")


########################################

# * * * * *
#   * * * *
#     * * *
#       * *
#         *

for i in range(n):
  for j in range(n):
    if i<= j:
      print('*', end =' ')
    else:
      print(' ', end= ' ')
  print()

print("--------------------")


# * * * * *
# *       *
# *       *
# *       *
# * * * * *

n=5
for i in range(n):
  for j in range(n):
    if i==0 or i== n-1 or j == 0 or j == n-1:
      print('*', end = ' ')
    else:
      print(' ', end= ' ')
  print()

print("--------------------")

# * * * * *
# *       *
# * * * * *
# *       *
# *       *
mid = n//2
for i in range(n):
  for j in range(n):
    if i==0 or i == mid or j == 0 or j == n-1:
      print('*', end = ' ')
    else:
      print(' ', end= ' ')
  print()

print("--------------------")

# * * * * *
# *       *
# * * * * *
# *       *
# * * * * *

mid = n//2
for i in range(n):
  for j in range(n):
    if i==0 or i == mid or i==n-1 or j == 0 or j == n-1:
      print('*', end = ' ')
    else:
      print(' ', end= ' ')
  print()

print("--------------------")

# * * * * *
# *
# *
# *
# * * * * *

for i in range(n):
  for j in range(n):
    if i==0 or i==n-1 or j == 0:
      print('*', end = ' ')
    else:
      print(' ', end= ' ')
  print()


print("--------------------")

# * * * * *
# *
# * * * * *
# *
# * * * * *
mid = n//2
for i in range(n):
  for j in range(n):
    if i==0 or i == mid or i==n-1 or j == 0:
      print('*', end = ' ')
    else:
      print(' ', end= ' ')
  print()

print("--------------------")

# * * * * *
# *
# * * * * *
# *
# * 
mid = n//2
for i in range(n):
  for j in range(n):
    if i==0 or i == mid or j == 0:
      print('*', end = ' ')
    else:
      print(' ', end= ' ')
  print()

print("--------------------")

# * * * * *
# *
# *   * * *
# *       *
# * * * * *
n=7
mid = n//2
for i in range(n):
  for j in range(n):
    if i==0 or (i == mid and j>mid) or i==n-1 or j == 0 or (j==n-1 and i>=mid):
      print('*', end = ' ')
    else:
      print(' ', end= ' ')
  print()

print("--------------------")

# *           *
# *           *
# *           *
# * * * * * * *
# *           *
# *           *
# *           *
n=7
mid = n//2
for i in range(n):
  for j in range(n):
    if j==0 or j==n-1 or i==mid:
      print('*', end = ' ')
    else:
      print(' ', end= ' ')
  print()

print("--------------------")

# * * * * * * *
#       *
#       *
#       *
#       *
#       *
# * * * * * * *
n=7
mid = n//2
for i in range(n):
  for j in range(n):
    if i==0 or i==n-1 or j==mid:
      print('*', end = ' ')
    else:
      print(' ', end= ' ')
  print()

print("--------------------")

# * * * * * * *
#       *
#       *
#       *
#       *
#       *
# * * * * 
n=7
mid = n//2
for i in range(n):
  for j in range(n):
    if i==0 or i==n-1 and j<=mid or j==mid:
      print('*', end = ' ')
    else:
      print(' ', end= ' ')
  print()



print("--------------------")

# *         *
# *       *
# *     *
# *   *
# * *
# * *
# *   *
# *     *
# *       *
# *         *
n=10
mid = n//2
for i in range(n):
  for j in range(n):
    if j==0 or i+j==mid or i-j==mid-1:
      print('*', end = ' ')
    else:
      print(' ', end= ' ')
  print()

print("--------------------")

# *                 *
# * *             * *
# *   *         *   *
# *     *     *     *
# *       * *       *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
n=10
mid = n//2
for i in range(n):
  for j in range(n):
    if j==0 or j==n-1 or (i+j==n-1 and j>= mid) or (i==j and j< mid) :
      print('*', end = ' ')
    else:
      print(' ', end= ' ')
  print()

print("--------------------")

# *                 *
# * *               *
# *   *             *
# *     *           *
# *       *         * 
# *         *       *
# *           *     *
# *             *   *
# *               * *
# *                 *
n=10
mid = n//2
for i in range(n):
  for j in range(n):
    if j==0 or j==n-1 or i==j:
      print('*', end = ' ')
    else:
      print(' ', end= ' ')
  print()

print("--------------------")

# * * * * * * * * * *
# *                 *
# *                 *
# *                 *
# *                 *
# *         *       *
# *           *     *
# *             *   *
# *               * *
# * * * * * * * * * *
n=10
mid = n//2
for i in range(n):
  for j in range(n):
    if i==0 or j==0 or i==n-1 or j==n-1 or i==j and j>=mid:
      print('*', end = ' ')
    else:
      print(' ', end= ' ')
  print()


