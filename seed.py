"""Seed file to make sample data for users db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
madScientist = User(first_name='Albert', last_name="Einstein", image_URL="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.7o-Gaf6oMuM3_XvLGQZuMgHaEo%26pid%3DApi&f=1&ipt=5d870e65b987e4c37adf92478dccbb9bcdfd53c96e579f6894b38367c950952f&ipo=images" )
theLegend = User(first_name='John', last_name="Legend", image_URL="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.f87gE5woYMAkIu8EwdAo3gHaJ4%26pid%3DApi&f=1&ipt=b03436f607d51ababe4e1c98bcc793c12f3b28e5b698e6ac5bfaba1fa5578039&ipo=images")
MrsSmith = User(first_name='Angelina', last_name="Jolie", image_URL="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.JQmhHObbPOyR3Yby55vydQHaLH%26pid%3DApi&f=1&ipt=446672fe600862ecd2e9322d7967401d508e5224667fd1175512cfbb31b92161&ipo=images")

# Add new objects to session, so they'll persist
db.session.add(madScientist)
db.session.add(theLegend)
db.session.add(MrsSmith)

# Commit--otherwise, this never gets saved!
db.session.commit()