from controller import UserController, BookmarkController, PublisherController, TagController

# User Controller Tests
userController = UserController()

userController.register('adnan@gmail.com')
userController.register('adnan2@gmail.com')
userController.register('adnan3@gmail.com')
userController.register('adnan4@gmail.com')

print(userController.login('adnan@gmail.com'))
print(userController.login('adnan2@gmail.com'))
print(userController.login('adnan6@gmail.com'))

# Bookmark Controller Tests
bookmarkController = BookmarkController()

user_id = 1  # Assume user with id 1 exists
publisher_id = 1  # Assume publisher with id 1 exists

print(bookmarkController.addBookmark(user_id, publisher_id))
print(bookmarkController.addBookmark(user_id, publisher_id + 1))

print(bookmarkController.getBookmarksByUserId(user_id))

# Publisher Controller Tests
publisherController = PublisherController()
tagController = TagController()

print(publisherController.register('Sports News'))
print(publisherController.register('Politics News'))
print(publisherController.register('Technology News'))

publisher_id_1 = 1  # Assume publisher with id 1 exists
tag_name_1 = 'sports'

print(tagController.addTag(publisher_id_1, tag_name_1))

publisher_name = 'Sports News'
tag_name_2 = 'politics'

print(publisherController.searchPublisherByName(publisher_name))
print(publisherController.searchPublisherByTag(tag_name_2))
