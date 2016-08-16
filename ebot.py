import time, re, praw, sqlite3

user_agent = 'A database bot to collect Reddit usernames'
app_id = ''
app_secret = ''
app_uri = 'https://127.0.0.1:65010/authorize_callback'
app_scopes = 'account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread'
refresh_token = ''


reddit = sqlite3.connnect('reddit.db')
cur = reddit.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS usernames(id TEXT)')
reddit.commit()

def save(author):
    author = '/u/'+author
    cur.execute('INSERT INTO usernames VALUES(?)', [author])
    reddit.commit()

def get_submissions(sub='all', posts=1000):
    submissions = r.get_submissions(sub).get_new(posts)
    for submission in submissions:
        author = submission.author.name.lower()
        cur.execute('SELECT * FROM usernames WHERE ID=?', [author])
        if not cur.fetchone():
            cur.execute('INSERT INTO usernames VALUES(?)', [author])
            print('Adding' + '/u/' + author ' to database')
            save()




while True:
    get_submissions()
    time.sleep(2)
