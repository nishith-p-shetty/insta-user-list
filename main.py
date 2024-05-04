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

with open('./index.html', 'w') as file:
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
				<th>Profile Picture</th>
				<th>Name</th>
				<th>Username</th>
				<th>Bio</th>
                <th>Post Count</th>
				<th>Followers</th>
				<th>Following</th>
				<th>Is Private</th>
			</tr>
            <tr>
                <td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>''')

with open('./index.html', 'a') as file:
    for idx, usrname in enumerate(i_flwng_oth_no_flbk):
        profile = instaloader.Profile.from_username(L.context, usrname)
        file.write(f'''
    			<tr>
                    <td>{idx}</td>
    				<td><a href="{profile.profile_pic_url}" target="_blank">Pic</a></td>
    				<td>{profile.full_name}</td>
    				<td>
    					<a href="https://www.instagram.com/{profile.username}/"target="_blank">{profile.username}</a>
    				</td>
    				<td>{profile.biography}</td>
    				<td>{profile.get_posts().count}</td>
    				<td>{profile.followers}</td>
    				<td>{profile.followees}</td>
    				<td>{profile.is_private}</td>
                </tr>''')

with open('./index.html', 'a') as file:
    file.write('''
		</table>
        <br>
        <br>
        <br>
        <table>
            <caption>To Follow</caption>
			<tr>
                <th>Sl. No.</th>
				<th>Profile Picture</th>
				<th>Name</th>
				<th>Username</th>
				<th>Bio</th>
                <th>Post Count</th>
				<th>Followers</th>
				<th>Following</th>
				<th>Is Private</th>
			</tr>
            <tr>
                <td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>''')

with open('./index.html', 'a') as file:
    for idx, usrname in enumerate(oth_flwing_me_no_flbk):
        profile = instaloader.Profile.from_username(L.context, usrname)
        file.write(f'''
    			<tr>
                    <td>{idx}</td>
    				<td><a href="{profile.profile_pic_url}" target="_blank">Pic</a></td>
    				<td>{profile.full_name}</td>
    				<td>
    					<a href="https://www.instagram.com/{profile.username}/"target="_blank">{profile.username}</a>
    				</td>
    				<td>{profile.biography}</td>
    				<td>{profile.get_posts().count}</td>
    				<td>{profile.followers}</td>
    				<td>{profile.followees}</td>
    				<td>{profile.is_private}</td>
                </tr>''')

with open('./index.html', 'a') as file:
    file.write('''
		</table>
	</body>
</html>''')