

# 1. Boş siyahı
empty_list = []

# 2. 5-dən çox elementli siyahı
my_list = [1, 2, 3, 4, 5, 6, 7]

# 3. Siyahının uzunluğu
print(len(my_list))  # 7

# 4. İlk, orta və son element
print(my_list[0])              # ilk → 1
print(my_list[len(my_list)//2])  # orta → 4
print(my_list[-1])             # son → 7

# 5. mixed_data_types
mixed_data_types = ['Əli', 25, 1.75, False, 'Bakı']

# 6. it_companies siyahısı
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Siyahını çap et
print(it_companies)

# 8. Şirkətlərin sayı
print(len(it_companies))  # 7

# 9. Birinci, orta və son şirkət
print(it_companies[0])                     # Facebook
print(it_companies[len(it_companies)//2])  # IBM
print(it_companies[-1])                    # Amazon

# 10. Şirkətlərdən birini dəyiş
it_companies[0] = 'Meta'
print(it_companies)

# 11. Yeni şirkət əlavə et
it_companies.append('Netflix')
print(it_companies)

# 12. Ortaya şirkət daxil et
it_companies.insert(len(it_companies)//2, 'Tesla')
print(it_companies)

# 13. IBM-dən başqa birini böyük hərflərlə dəyiş
it_companies[1] = it_companies[1].upper()  # GOOGLE
print(it_companies)

# 14. '#;' ilə birləşdir
print('#;'.join(it_companies))

# 15. Şirkətin siyahıda olub olmadığını yoxla
print('Apple' in it_companies)   # True
print('Twitter' in it_companies) # False

# 16. Siyahını sırala
it_companies.sort()
print(it_companies)

# 17. Tərsinə çevir
it_companies.reverse()
print(it_companies)

# 18. İlk 3 şirkət
print(it_companies[:3])

# 19. Son 3 şirkət
print(it_companies[-3:])

# 20. Orta şirkət(lər)
mid = len(it_companies) // 2
print(it_companies[mid:mid+1])

# 21. İlk şirkəti çıxar
it_companies.pop(0)
print(it_companies)

# 22. Orta şirkəti çıxar
mid = len(it_companies) // 2
it_companies.pop(mid)
print(it_companies)

# 23. Son şirkəti çıxar
it_companies.pop()
print(it_companies)

# 24. Bütün şirkətləri çıxar
it_companies.clear()
print(it_companies)  # []

# 25. Siyahını məhv et
del it_companies

# 26. Siyahıları birləşdir
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
combined = front_end + back_end
print(combined)

# 27. Kopyala və Python, SQL əlavə et
full_stack = combined.copy()
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')
print(full_stack)
