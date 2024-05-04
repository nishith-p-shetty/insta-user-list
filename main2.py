import instaloader

USERNAME='XXXXXXXXXXX'
PASSWORD='XXXXXXXXXXX'

L = instaloader.Instaloader()

L.login(USERNAME, PASSWORD)

FOLLOWERS=[]
FOLLOWING=[]
i_flwng_oth_no_flbk=[]
oth_flwing_me_no_flbk=[]

profile = instaloader.Profile.from_username(L.context, USERNAME)

for follower in profile.get_followers():
    FOLLOWERS.append(follower.username)

for followee in profile.get_followees():
    FOLLOWING.append(followee.username)

for i in FOLLOWERS:
    if i not in FOLLOWING:
        oth_flwing_me_no_flbk.append(i)

for i in FOLLOWING:
    if i not in FOLLOWERS:
        i_flwng_oth_no_flbk.append(i)

with open('./index1.html', 'w') as file:
    file.write('''<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>Insta-Useer-List</title>
		<style>
			table,
			th,
			td {
				border: 2px solid black;
                border-collapse: collapse;
                border-radius: 10px;
                padding: 15px;
			}
		</style>
	</head>
	<body>
		<table>
            <caption>To Unfollow</caption>
			<tr>
                <th>Sl. No.</th>
				<th>Username</th>
			</tr>
            <tr>
                <td></td>
				<td></td>
			</tr>''')

with open('./index1.html', 'a') as file:
    for index, usrname in enumerate(i_flwng_oth_no_flbk):
        profile = instaloader.Profile.from_username(L.context, usrname)
        file.write(f'''
    			<tr>
                    <td>{index+1}</td>
    				<td>
    					<a href="https://www.instagram.com/{profile.username}/"target="_blank">{profile.username}</a>
    				</td>
                </tr>''')

with open('./index1.html', 'a') as file:
    file.write('''
		</table>
        <br>
        <br>
        <br>
        <table>
            <caption>To Follow</caption>
			<tr>
                <th>Sl. No.</th>
				<th>Username</th>
			</tr>
            <tr>
                <td></td>
				<td></td>
			</tr>''')

with open('./index1.html', 'a') as file:
    for index, usrname in enumerate(oth_flwing_me_no_flbk):
        profile = instaloader.Profile.from_username(L.context, usrname)
        file.write(f'''
    			<tr>
                    <td>{index+1}</td>
    				<td>
    					<a href="https://www.instagram.com/{profile.username}/"target="_blank">{profile.username}</a>
    				</td>
                </tr>''')

with open('./index1.html', 'a') as file:
    file.write('''
		</table>
	</body>
</html>''')