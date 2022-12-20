# from tqdm import trange

# offset = 9
# x = 1_000_000_000_000 - offset
# # 581395348 * i
# i = 1720
# c = 2738

# times, rest = divmod(x, i)

# final = c * times
# final = i * times
# final += i


# # 3151 =  5010
# # 4871 =  7748
# # 6591 = 10486
# # MUST BE HIGHER THAN: 1_591_860_460_086


from tqdm import trange

X = 0
for i in trange(1_000_000_000_000):
    X + 1

print(X)
