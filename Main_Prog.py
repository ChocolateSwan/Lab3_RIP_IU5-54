
import Client
#james.hetfield
#id87295617
#kshmax
#msavelyeva96
#del: 13
user = Client.Client ("http://api.vk.com/method","users.get")
user.params="user_ids="+input('Введите username или vk_id пользователя: ')
resp_user=user.execute()
id=user.find_id(resp_user.text)
print("Ваш id: ",id)
friends=Client.Client("http://api.vk.com/method","friends.get")
friends.params="user_id="+id+"&fields=bdate"
resp_friends=friends.execute()
friends.build_gist(resp_friends)


