"""Message model tests."""

import os
from unittest import TestCase

from models import db, User, Message, Follows, Like
from sqlalchemy.exc import IntegrityError
from datetime import datetime

# set an environment variable
# to use a different database for testing (do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"

# Now import app

from app import app

# Create tables (do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create new test data

db.create_all()


USER_DATA = {
    "email":"test@test.com",
    "username":"testuser",
    "password":"HASHED_PASSWORD"
}



class MessageModelTestCase(TestCase):
    """ Tests for message model """

    def setUp(self):
        """ create client """

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()
        Like.query.delete()

        self.client = app.test_client()

        user = User(**USER_DATA)

        db.session.add(user)
        db.session.commit()
        
        self.user = user

        message_data = {
            "user_id":self.user.id,
            "text":"test"
        }

        message = Message(**message_data)
        db.session.add(message)
        db.session.commit()

        self.message = message
        
    def tearDown(self):
        """ Clean up fouled data """

        db.session.rollback()

    def test_message_model(self):
        """ Test if the message model works? """
        # TODO: test self.user.messages is equal to [self.message]
        self.assertEqual(len(self.user.messages), 1)
        self.assertEqual(Message.query.count(), 1)

        self.assertEqual(self.message.text, "test")
        self.assertEqual(self.message.user_id, self.user.id)
        self.assertIsInstance(self.message.timestamp, datetime)

        self.assertEqual(self.message.user, self.user)

    def test_message_model_fail(self):
        """ Is no message created when non-nullable argument is not passed in 
        """
        with self.assertRaises(IntegrityError):
            message = Message(user_id=self.user.id)
            db.session.add(message)
            db.session.commit()

        db.session.rollback()

        self.assertEqual(Message.query.count(), 1)