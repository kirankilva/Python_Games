def flames_game(user1, user2):
    rule_list = ['Friends', 'Love', 'Affection', 'Marriage', 'Enemy', 'Siblings']
    new_user1 = list(user1)
    new_user2 = list(user2)

    if len(user1) < len(user2):
        for i in user1:
            if i in new_user2:
                new_user1.remove(i)
                new_user2.remove(i)
    else:
        for j in user2:
            if j in new_user1:
                new_user1.remove(j)
                new_user2.remove(j)

    count = len(new_user1 + new_user2)
    if count > 0:
        while len(rule_list) > 1:
            count = len(new_user1 + new_user2) % len(rule_list) - 1
            if count >= 0:
                rule_list = rule_list[count+1:] + rule_list[:count]
            else:
                rule_list = rule_list[:len(rule_list)-1]
        return f"Relationship Status : {rule_list[0]}"
    return 'Try with different names'

  
  
person1 = input('Enter the name: ').lower().replace(' ', '')
person2 = input('Enter the name: ').lower().replace(' ', '')
status = flames_game(person1, person2)
print(status)
