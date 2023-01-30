from instabot import Bot
bot = Bot() #intializing the bot with inbuilt function
#login
bot.login(username= " ", password= " "  )
#follow a user
bot.follow(" ") #pass user_id
#follow a multiple users
bot.follow_users([" ", " "])
#unfollow the non followers
bot.unfollow_non_followers(" ") #pass user_id
#upload a photo
bot.upload_photo(" ", caption = " " )
#pass the location and name of the image
#upload photo as a story
bot.upload_story_photo(" ")
#pass the location and name of the image
#write the path with changinf slashes along with name
#unfollow a user
bot.unfollow("username")
#pass username
#sending a msg to multiple users
bot.send_message("msg",["username1", "username2"])
#like a post
bot.like_user(" ", amount =4, filtration=False)  #amount says the latest 4 posts
#username, how many posts to like
#comment
user_id = bot.get_user_id_from_username(" ") #give user name
media_id = bot.get_last_user_medias(user_id, 1) #media_id to get select post with latest count
bot.comment(media_id[0], "You are too cute")
#getting the user followers
followers_list = bot.get_user_followers(" ") #pass user id
following_list = bot.get_user_following(" ") #pass user id
for each_follower in followers_list:
    print(bot.get_username_from_user_id(each_follower))
for each_following in following_list_list:
    print(bot.get_username_from_user_id(each_following))
# prints the values of the users one by one

#conclusion
#The difficulty I faced is in selecting the post to comment I was able
#comment only the latest post of the user




