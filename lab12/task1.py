import redis
from faker import Faker
import random


fake = Faker()
r = redis.Redis(
    host = 'redis-12057.c262.us-east-1-3.ec2.cloud.redislabs.com',
    port='12057',
    password='NB6T0nUzf6jhGW78z5yshkt2Fl0T0FNp')

customer = []

for i in range(6):
    name = fake.name().split(" ")
    customer.append("customer:00"+str(i))
    r.hset("customer:00"+str(i), mapping={"first_name": name[0], "second_name": name[1]})



for i in range(8):
    r.hset("order:100" + str(i), mapping={"customer":random.choice(customer) ,
                                           "order_date": fake.date(),
                                           "order_total":str(fake.random.randint(0,100))})




for i in range(6):
    print(r.hgetall("customer:00"+str(i)))

for i in range(8):
    print(r.hgetall("order:100"+str(i)))



