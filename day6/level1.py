
# 1. Boş tuple
empty_tuple = ()

# 2. Bacılar və qardaşlar
sisters = ('Aynur', 'Leyla')
brothers = ('Tural', 'Murad')

# 3. Birləşdir
siblings = sisters + brothers
print(siblings)  # ('Aynur', 'Leyla', 'Tural', 'Murad')

# 4. Neçə qardaş-bacın var?
print(len(siblings))  # 4

# 5. Tuple dəyişilməzdir, ona görə siyahıya çevir → əlavə et → yenidən tuple et
family_members = list(siblings)
family_members.append('Əli')    # Ata
family_members.append('Günel')  # Ana
family_members = tuple(family_members)
print(family_members)  # ('Aynur', 'Leyla', 'Tural', 'Murad', 'Əli', 'Günel')
