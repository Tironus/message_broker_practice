import redis

r = redis.Redis(host='localhost', port=6379, db=0)
p = r.pubsub()
p.subscribe('my-first-channel')
for i in range(100000):
    r.publish('my-first-channel', 'some data')
p.unsubscribe()