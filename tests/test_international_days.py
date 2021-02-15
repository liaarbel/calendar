from datetime import date

import pytest

from app.database.models import InternationalDays
from app.internal import international_days
from app.internal.json_data_loader import load_data
from app.internal.utils import create_model, delete_instance

DATE = date(2021, 6, 1)
DAY = "Hamburger day"
ALL_DATES = [(7, 3), (16, 9), (19, 4), (20, 7), (21, 6), (8, 5), (10, 7), (14, 1), (15, 4), (26, 12), (3, 2), (27, 1), (4, 5), (28, 10), (29, 11), (18, 10), (8, 12), (22, 12), (9, 9), (23, 9), (14, 8), (12, 8), (3, 11), (27, 6), (4, 12), (28, 1), (2, 12), (5, 1), (29, 4), (16, 7), (17, 6), (18, 5), (21, 8), (22, 7), (23, 6), (10, 9), (11, 4), (12, 7), (15, 10), (13, 6), (24, 2), (25, 3), (4, 11), (2, 7), (5, 10), (6, 1), (7, 4), (19, 1), (24, 9), (25, 4), (26, 3), (27, 10), (30, 5), (16, 11), (19, 6), (17, 10), (20, 1), (21, 4), (8, 7), (22, 11), (9, 6), (10, 5), (11, 8), (14, 7), (15, 6), (26, 10), (3, 4), (27, 3), (30, 12), (4, 7), (28, 4), (5, 6), (29, 9), (16, 2), (17, 3), (20, 8), (18, 8), (22, 2), (23, 11), (10, 12), (11, 1), (12, 10), (13, 11), (28, 3), (2, 10), (29, 2), (6, 12), (17, 4), (7, 9), (18, 3), (22, 5), (11, 6), (12, 1), (13, 4), (24, 4), (1, 6), (25, 1), (2, 5), (26, 6), (5, 8), (6, 7), (7, 6), (31, 5), (19, 3), (20, 4), (8, 2), (9, 3), (24, 11), (14, 2), (25, 10), (26, 1), (3, 1), (27, 12), (30, 11), (19, 8), (17, 8), (20, 3), (21, 2), (8, 9), (22, 9), (9, 4), (23, 12), (10, 3), (11, 10), (14, 5), (26, 8), (3, 6), (27, 5), (1, 10), (4, 1), (28, 6), (5, 4), (29, 7), (16, 4), (6, 11), (17, 1), (20, 10), (18, 6), (21, 11), (23, 5), (10, 10), (11, 3), (14, 12), (12, 4), (15, 9), (13, 9), (1, 3), (4, 8), (2, 8), (6, 2), (7, 11), (18, 1), (23, 2), (12, 3), (13, 2), (24, 6), (1, 4), (25, 7), (2, 3), (26, 4), (27, 9), (6, 5), (30, 6), (31, 7), (16, 8), (19, 5), (20, 6), (21, 7), (8, 4), (9, 1), (10, 6), (25, 8), (15, 5), (3, 3), (30, 9), (4, 4), (28, 9), (31, 12), (29, 12), (19, 10), (8, 11), (9, 10), (10, 1), (11, 12), (14, 11), (15, 2), (3, 8), (27, 7), (1, 8), (4, 3), (5, 2), (29, 5), (16, 6), (6, 9), (17, 7), (7, 12), (18, 4), (21, 9), (22, 6), (23, 7), (10, 8), (11, 5), (12, 6), (15, 11), (13, 7), (24, 1), (1, 1), (4, 10), (2, 6), (5, 11), (7, 5), (24, 8), (25, 5), (2, 1), (26, 2), (27, 11), (30, 4), (28, 12), (7, 2), (31, 1), (16, 10), (19, 7), (17, 11), (21, 5), (8, 6), (22, 10), (9, 7), (10, 4), (11, 9), (14, 6), (15, 7), (3, 5), (4, 6), (28, 11), (5, 7), (29, 10), (16, 1), (19, 12), (17, 12), (18, 11), (9, 8), (23, 8), (14, 9), (12, 9), (15, 12), (13, 12), (3, 10), (28, 2), (29, 3), (17, 5), (18, 2), (22, 4), (23, 1), (11, 7), (13, 5), (24, 3), (1, 7), (25, 2), (2, 4), (5, 9), (6, 6), (30, 3), (7, 7), (8, 1), (24, 10), (25, 11), (30, 10), (31, 3), (16, 12), (19, 9), (17, 9), (20, 2), (21, 3), (8, 8), (22, 8), (9, 5), (10, 2), (11, 11), (14, 4), (12, 12), (25, 12), (15, 1), (26, 11), (3, 7), (27, 2), (1, 11), (28, 5), (31, 8), (5, 5), (29, 8), (16, 3), (6, 10), (17, 2), (20, 9), (18, 9), (21, 12), (22, 3), (23, 10), (12, 11), (13, 10), (3, 12), (1, 12), (2, 11), (29, 1), (7, 8), (23, 3), (12, 2), (13, 3), (24, 5), (1, 5), (2, 2), (26, 7), (6, 4), (30, 1), (7, 1), (19, 2), (20, 5), (8, 3), (9, 2), (24, 12), (14, 3), (25, 9), (30, 8), (28, 8), (19, 11), (20, 12), (18, 12), (21, 1), (8, 10), (9, 11), (14, 10), (15, 3), (26, 9), (3, 9), (27, 4), (1, 9), (4, 2), (28, 7), (31, 10), (5, 3), (29, 6), (16, 5), (6, 8), (20, 11), (18, 7), (21, 10), (22, 1), (9, 12), (23, 4), (10, 11), (11, 2), (12, 5), (15, 8), (13, 8), (1, 2), (4, 9), (2, 9), (5, 12), (6, 3), (7, 10), (13, 1), (24, 7), (25, 6), (26, 5), (27, 8), (30, 7)]
ALL_DAYS = ['Toast day and Chilli day', 'Marriage day and Ferris Wheel day', 'Moon day and International chess day', 'Science Ficyion Day and World introvert day', 'International Tug-of-War day and Chocolate mint day', 'Joke day and Gingersnap day', 'Toy camera day and Spreadsheet day', 'Carrot cake day and Golden retriver day', 'Darwin day and No one eats alone day', 'World meditation day and I need a patch for that day', 'World play your ukulele day and Tater tot day', 'Apricot Day and Balloon Ascension day', 'Happy hour day and Chicken soup for the soul day', 'World food day and Dictionary day', 'Morse code day and Tell a story day', 'World poetry day and Vermouth day', 'Star terk day and Pardon day', 'Sticker day and Rubber duckie day', "Nail day and Internatinal midwive's day", 'World Elephant day and Vinyl record day', 'World whisky day and Chocolate chip day', 'Hug a drummer day and SHIFT10 day', 'Seocial media day and Metheor watch day', 'Scrubs day and Beer and pizza day', 'No dirty dishes day and Museum day', 'Popcorn day and Tin can day', 'Brownie day and Lard day', 'Work from home day and International Day Against Homophobia and Transphobia and Biphobia', 'Eat a hoagie day and Cream filled doughnut day', 'World plumbing day and Oatmeal nut waffles day', 'World laughter day and Baby day', 'World Octopus day and Egg day', 'World television day and Red mitten day', 'Moscato day and Lost sock memorial day', 'Cookie day and International cheetah day', 'International day of happines and Quilting day', 'Mint julep day and Water a flower day', 'Jewel day and Ken day', 'Burger day and Dog day', 'World teachers day and Chic spy day', 'Star wars day and 45 day', 'Bacon day and Bicarbonate of soda day', 'Read across america day and Old stuff day', 'Independence from meat day and Jackfruit day', 'Scream day and Pig in a blanket day', 'International red panda day and Cheeseburger day', 'Martini day and Juggling day', 'Buy nothing day and Flossing day', 'No bra day and Train your brain day', 'Kebab day and Sugar cookie day', 'International orangutan day and Photography day', "Lips appreciation day and St.urho's day", 'Yorkshire pudding day and Wava all your fingers at your neighbors day', 'Rollercoaster day and Rum day', 'Hippo day and Annoy squidward day', 'DIY day and Chocolate mousse day', 'World freedom day and Chaos never dies day', 'Stress awareness day and Sandwich day', 'Air conditioning appreciation day and Eat beans day', 'Turtle day and Lucky penny day', 'Skyscraper day and Bring your manners to work day', 'Bathtub day and Frappe day', 'Ferret day and Walk to work day', "Blueberry cheesecake day and Beautician's day and World refrigeration day", "Golfer's day and International safety pin day", 'World vegan day and Go cook for your pets day', 'Lemonade day and Garden meditation day', "Saint Patrick's day", 'Drink beer day and International poke day', 'Aunt and uncle day and Coffee milk shake day', 'Drive-thru day and Tequila day', 'Milk chocolate day and World hepatitis day', 'Card playing day', 'Star trek first contact day and Read a road map day', "Business women's day and World car free day", 'Biscuit day and Paper clip day', 'World kindness day and Indian pudding day', 'Poinsettia day and Gingerbread house day', 'World water day and Gryffindor pride day', 'Drawing day and Sea monkey day', 'Math 2.0 day and Chocolate with almonds day', 'Hat day and Bagel day', 'International dance day and We jump the world day', 'Coast guard day and International clouded leopard day', 'World suicide prevention day and TV dinner day', 'Love your pet day and Pangolin day', 'Pumpkin pie day', 'Crayola Crayon day and World backup day', 'Talk like Shakespeare day and Asparagus day', 'Ask a stupid question day and International podcast day', 'International artist day and Accounting day', 'Junk food day and Lamington day', 'Have a party with your bear day and Clarinet day', 'World smile day and International coffee day', 'Daiquiri day and Get out of the doghouse day', 'Let it go day and International widows day', 'Nothong day and Religious freedom day', 'Chocolate ice cream day and VCR day', 'Thank a letter carrier day and World cancer day', 'Bad poetry day and Never give up day', 'Peanut butter and chocolate day and Sprinkle day', 'Pie day and Visit your local quilt shop day', 'Magic day and Caramel apple day', "Ditch new year's resolutions day and Kid inventor's day", 'Windmill day and No socks day', 'Coming out day and Canadian thanksgiving', 'Melba toast day and Puppy day', 'Trivia Day and Weigh-in day', 'Bittersweet chocolate with almonds day and Zero tasking day', 'Use your common sense day and Men make dinner day', 'World wildlife day and What if cats and dogs had opposable Thumbs day', "World nutella day and Weatherperson's day", 'Tuba day and Therapeutic massage awareness day', 'Hairball awareness day and honesty day', 'Beer day and No housework day', 'International kissing day and Fried chicken day', 'Pick strawberries day and World bee day', 'Make cut-out snowflakes day and Fruitcake day', 'Walk on stilts day and Norfolk day', 'Eat a red apple day and Day without art day', 'Guacamole day and Play doh day', 'Tourism day and Corned beef hash day', 'Global beatles day and Take your dog to work day', 'Fun day and Tell a lie day', 'Monkey day and Roast chestnuts day', 'Tooth fairy day and Floral Design day', "Name your PC day and Universal children's day", "Doctor's day and Take a walk in the park day", 'Bow tie day and Franchise appreciation day', 'Ice cream soda day and World refugee day', 'Slinky day and Amagwinya day', 'Ugly christmas sweater day and Maple syrup day', 'World blood donor day and Flag day', 'Best friends day and World oceans day', 'Chocolate covered raisins day and Flatmates day', 'French toast day and Aura awareness day', 'Mother ocean day and Stay up all night night', 'World tapas day and Fresh Veggies day', 'Senior health and fitness day and Paper airplane day', 'Shades day and Chicken dance day', "World table tennis day and New beer's eve", 'Hug an australian day and Burlesque day', 'Building and code staff appreciation day and Tofu day', 'Whipped Cream day and Bird Day', 'International body piercing day and Logistics day', 'Numeracy day and Top gun day', 'Tempura day and Bobblehead day', 'World music day and International yoga day', 'World heart day and Biscotti day', 'May ray day', 'Particularly preposterous packing day and Aged care employee day', 'Black cat day and Cranky co-workers day', 'Make a difference day and Ipod day', 'Chocolate cake day and World breast pumping day', 'Punch day and Pepperoni pizza day', 'Canadian beer day and Mad hatter day', 'Re-gifting day and Chocolate covered anything day', "World alzheimer's day and Escapology day", 'Be heard day and Plant power day', 'Disc jockey day and Cheese lovers day', 'Superman day and World gin day', 'Shark awareness day and Mac & cheese day', 'World thinking day and Single tasking day', 'Eat what you want day and World ego awareness day', "Vitamin C day and Geologist's day", 'Dessert day and International top spinning day', 'Meatball day and Barbie day', 'Random acts of kindness day and World human spirit day', 'Cat herders day and Lemon cupcake day', 'Cotton candy day and Pearl harbor remembrance day', 'Barista day and Fun facts about names day', 'Eat your vegetables day and Garbage man day', 'Dress up your pet day and International Kite day', 'Backward day and Gorilla suit day', 'Zoo lovers day and Pygmy hippo day', 'Pack your lunch day and International wig day', 'Lumberjack day and Rivers day', "Miner's day and Walt disney day", "Restless legs awareness day and Za'atar day and Fitness day", 'Say something nice day', 'Deskfast day and Hamster day', 'Bicycle day and Hanging out day', 'Lazy day and World lion day', 'Yarn Bombing day and Corn of the cob day', "White chocolate cheesecake day and dentist's day", 'Inane answering message day and Seed swap day', 'Make up your mind day and Champagne day', 'Unites nation day and Mother in law day', 'Tiara day and Escargot day', 'Teach your children to save day and Earth day', 'Step in a puddle and splash your friends day and Heritage treasures day', 'Sisters day and Planner day', 'Sardines day and Jukebox day', "World student's day and Chicken cacciatore day", 'Chocolates day and Lemon cream pie day', 'Check the chip day and Relaxation day', 'Guinea pig appreciation day and Corn fritters day', 'Raspberry cake day and Uncommon Instrument awareness day', 'Espresso day and Fibonacci day', 'Bomb pop day and Swim in lap day', 'World orphans day and World quality day', 'Curling is cool day and Play tennis day', "World duchenne awareness day and Beer lover's day", 'Girls scout day and International fanny pack day', 'Tradesmen day and International country music day', 'Hammock day and CrÃ¨me brulee day', 'Senior citizen day and World honey bee day', 'World emoji day and Peach ice cream day', 'World creativity and innovation day and World stationery day', 'Evaluate your life day and International gin and tonic day', "Men's grooming day and International day of medical transporters", 'Scrabble day and Internatinal FND Awareness day', 'Unicorn day and ASMR day', "Wine and cheese day and Parent's day", 'Australia day and Peanut brittle day', 'Pina colada day and Teddy bear picnic day', "International men's day and World toilet day", 'Ice cream sandwich day and Coloring book day', 'International picnic day and Go fishing day', 'Fresh breath day and International beer day', 'Umbrella day and Plimsoll day', 'Tap dance day and Towel day', 'Dolphin day and Day of pink', 'Melon day and Rice pudding day', 'Watermelon day and White wine day', 'Pink day and Tortilla chip day', 'Name your car day and World farm animals day', 'RosÃ© day and Donald duck day', 'No tabbaco day and Save your hearing day', 'Chocolate day and Macaroni day', "Receptionist's day and Limerick day", 'Fortune cookie day and Boss/Employee exchange day', 'International cat day and Happiness happens day', 'Talk like a priate day and Butterscotch pudding day', 'Chili dog day and International tiger day', 'Nature photography day and Beer day Britain', 'Waffle iron day and Camera day', 'Cuban sandwich day and Ride the wind day', 'Haiku poetry day and Blah blah blah day', 'Thrift shop day and Vanilla custard day', 'Roast leg of lamb day and Public gardens day', 'Sewing machine day and World softball day', 'Go for a ride day and Cranberry relish day', 'Homemade bread day and Unfriend day', 'Sausage roll day and Coworking day', 'World sleep day and Poultry day', 'World rainforest day and Onion rings day', 'International lego day and Global community engagement day', 'Grammar day and Marching band day', 'Pizza day and Safer internet day', 'Babble bath day and Joy Germ day', 'Eggnog day', 'Baked alaska day and World read aloud day', 'Beer can appreciation day and Peanut Butter day', 'Be an angel day and Eat a peach day', 'Etch a sketch day and New conversations day', 'Pokemon day and World NGO day', 'Kiss a ginger day and Marzipan day', 'Chocolate cupcake day and Developmental language disorder awareness day', 'Trail mix day and Overdose awareness day', 'Old farmers day and Own business day', 'Read a book day and Mouthguard day', 'Good hair day and Purple day', 'Nachos day and Numbat day', 'Deviled egg day and Dynamic harmlessness day', 'Computer security day and Mousse day', 'Look for an evergreen day and Oatmuffin day', 'Bake cookies day and Roast suckling pig day', 'Humbug day and Flashlight day', 'Fritters day', 'Awkward moments day and Companies that care day', 'Pineapple day and Sunglasses day', 'Operating room nurse day and Tongue twister day', 'Waffle day and Tolkien Reading day', 'More herbs less salt day and Potteries bottle oven day', 'Iced tea day and Jerky day', 'Origami day and Sundae day', 'Innovation day and Tim Tam day', 'Drink wine day and Pluto day', 'International strange music day and Knife day', 'International bat night and Banana lovers day', 'Roots day and Festivus day', 'Have a bagel day and Noodle ring day', 'Thank you note day and Candy cane day', 'Fat food day and Peppermint patty day', 'Clean out your refigerator day and Bundt cake day', 'Pet day and Cheese fondue day', 'International ninja day and Repeal day', 'Kiss and make up day and Banana split day', 'Pinata day and Columnists day', 'Pinhole photography day and Hug a plumber day', 'Peculiar people day and Bittersweet Chocolate day', 'World bicycle day and Chocolate maccaroon day', 'Violin day and Day of the horse', 'World calligraphy day and Son and daughter day', 'Superhero day and Stop food waste day', 'Make your bed day and Drive your studebaker day', 'Sun screen day and World product day', "Hug a vegetarian day and Lash stylist's day", 'Wildlife day and Macadamia nut day', 'Howl at the moon day and Pumpkin day', 'Pastry day and Techno day', 'Housing day and Social enterprise day', 'Animation day and Internet day and Cat day', 'Caps lock day and International stuttering awareness day', 'Take your child to the libray day and Frozen yogurt day', 'Fun at work day and Puzzle day', 'Work like a dog day and Blogger day', 'Neighbor day and Black forest cake day', 'Teddy bear day and Wienerschnitzel day', 'International chef day and International sloth day', 'Anisette day and World UFO day', 'Drinking straw day and Festival of sleep day', 'Cuddle up day and Bean Day', 'French fries day and Cow appreciation day', 'World dream day', 'Caviar day and Insurance nerd day', 'World speech day and World consumer rights day', 'Creamsicle day and Tattoo removal day', 'Extra day in leap year', 'World afro day and Cheese toast day', 'Shopping reminder day and Parfait day', 'Go caroling day and Games day', 'Be late for something day and World samosa day', 'Video games day and Hug your hound day', 'Sticky bun day and World whale day', 'Bavarian cream pie day and Pins and Needles day', 'No diet day and Password day', 'Gardening exercise day and Cancer survivors day', 'Calendar adjustment day and V-J day', 'Hugging day and Playdate day', "Plush animal lover's day", 'Husband Appriciations day and High five day', 'Vodka day and World habitat day', 'Thesaurus day and Martin luther king day', 'Day of unplugging and World book day', 'Sherlock Holmes day and Goth day', 'Blueberry muffin day and World population day', 'Wear your pajamas to work day and Save the elephant day', 'Blame someone else day and International lefthanders day', 'Apple day and Get smart about cerdit day', 'Gummi worm day and Hot dog day', 'Rocky road day and Running day', "Techies day and Boyfriend's day", "Answer your cat's Questions day and Hot sauce day", 'Radio day and Tortellini day', 'Learn about butterflies day and Pi day', 'Human rights day and Lager day', "Date nut bread day and Forefather's day", 'Bubble warp appreciation day and Opposite day', 'Apple turnover day and Bikini day', 'Lemon chiffon cake day and Niagara falls runs dry day', 'Sesame street day and Top up day', 'Checklist day and Hug a sheep day', 'Earth hour and International whiskey day', 'Cheesecake day and Friendship day', "International women's day and Peanut cluster day", 'Ring a bell day and Copyright Law day', 'Clean out your computer day and Molasses bar day', 'Volunteer recognition day and Chinese language day', 'Tick Tock day and Pepper pot day', 'Love your red hair day and Love your lawyer day', 'Amnesty international day and Hamburger day', 'Levi Strauss day and Personal chef day', 'Hug your cat day and Doughnut day', 'Bartender appreciation day and Make a gift day']


def open_resource(path):
    all_dates = []
    with open(path, 'r') as json_reader:
        days_json = json_reader.read()
        for day in days_json:
            all_dates.append((day["day"], day["month"]))
    return all_dates



@pytest.fixture
def international_day(session):
    inter_day = create_model(
        session, InternationalDays, id=1, day=1, month=6,
        international_day="Hamburger day"
    )
    yield inter_day
    delete_instance(session, inter_day)


@pytest.fixture
def all_international_days(session):
    load_data(session, 'app/resources/international_days.json',
              InternationalDays,
              international_days.create_international_day_object)
    all_international_days = list(set(list(session.query(InternationalDays))))
    yield all_international_days
    for day in all_international_days:
        delete_instance(session, day)


def test_input_day_equal_output_day(session, international_day):
    inter_day = international_days.get_international_day_per_day(
        session, DATE).international_day
    assert inter_day == DAY


def test_international_day_per_day_no_international_days(session):
    assert international_days.get_international_day_per_day(session,
                                                            DATE) is None


def test_all_international_days_per_day(session, all_international_days):
    count = 0
    for day in all_international_days:
        assert day.day, day.month == ALL_DATES[count]
        assert day.international_day == ALL_DAYS[count]
        count += 1