#!/usr/bin/env python3
"""CaptionCraft - draft social media captions and hashtag sets from the command line.

A tiny, dependency-free tool for small businesses and solo marketers.
Give it a topic, a business niche and a platform, and it prints ready
to post caption options with a matching hashtag set.

Usage:
    python3 captioncraft.py --topic "fresh sourdough" --niche bakery --platform instagram
    python3 captioncraft.py --topic "new brunch menu" --niche cafe --platform facebook --count 3
"""

import argparse
import random
import sys

HASHTAG_BANK = {
    "cafe": ["#CafeLife", "#CoffeeLovers", "#ButFirstCoffee", "#CafeVibes",
             "#SpecialtyCoffee", "#BrunchTime", "#CoffeeGram", "#LocalCafe"],
    "restaurant": ["#Foodie", "#InstaFood", "#FoodLover", "#EatLocal",
                   "#FoodGram", "#TastyEats", "#DinnerTime", "#FoodPhotography"],
    "bakery": ["#BakeryLife", "#FreshFromTheOven", "#BakersOfInstagram", "#Sourdough",
               "#PastryLover", "#BakedFreshDaily", "#CakeLovers", "#BreadLovers"],
    "salon": ["#SalonLife", "#HairGoals", "#BeautySalon", "#FreshCut",
              "#HairStylist", "#GlowUp", "#BeautyCare", "#SelfCareDay"],
    "gym": ["#FitnessMotivation", "#GymLife", "#TrainHard", "#FitFam",
            "#WorkoutMotivation", "#HealthyLifestyle", "#StrongNotSkinny", "#NoExcuses"],
    "realestate": ["#RealEstate", "#PropertyForSale", "#DreamHome", "#HouseHunting",
                   "#NewListing", "#HomeSweetHome", "#PropertyInvestment", "#JustListed"],
    "general": ["#SmallBusiness", "#SupportLocal", "#LocalBusiness", "#ShopLocal",
                "#EntrepreneurLife", "#BusinessOwner", "#CommunityFirst", "#MadeWithLove"],
}

HOOKS = [
    "Stop scrolling. {topic} just landed.",
    "You asked, we delivered: {topic}.",
    "POV: you finally tried {topic}.",
    "Three words: {topic}. That is the post.",
    "Warning: {topic} may cause serious cravings.",
    "Nobody talks about {topic} enough. Time to fix that.",
    "This is your sign to check out {topic}.",
    "Behind the scenes of {topic}. This one is special.",
]

BODIES = [
    "Made fresh, made with care, made for you. Come and see what the fuss is about.",
    "Small batch, big flavour, zero shortcuts. That is how we do things here.",
    "Tag someone who needs this in their life today.",
    "Available now - and when it is gone, it is gone.",
    "Quality you can feel from the first minute. Come as you are, leave happier.",
    "We put the work in so all you have to do is enjoy it.",
]

CALLS_TO_ACTION = {
    "instagram": "Save this post and tag a friend who would love it.",
    "facebook": "Share this with someone who needs to see it, and tell us what you think in the comments.",
    "linkedin": "What is your take? Share your thoughts in the comments.",
    "tiktok": "Follow for more, and tell us in the comments what to try next.",
}

PLATFORM_HASHTAG_LIMIT = {
    "instagram": 12,
    "facebook": 5,
    "linkedin": 5,
    "tiktok": 6,
}


def build_caption(topic, niche, platform, rng):
    hook = rng.choice(HOOKS).format(topic=topic)
    body = rng.choice(BODIES)
    cta = CALLS_TO_ACTION[platform]
    tags = list(HASHTAG_BANK[niche]) + list(HASHTAG_BANK["general"])
    rng.shuffle(tags)
    limit = PLATFORM_HASHTAG_LIMIT[platform]
    tags = tags[:limit]
    return "{hook}\n\n{body}\n\n{cta}\n\n{tags}".format(
        hook=hook, body=body, cta=cta, tags=" ".join(tags)
    )


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Draft social media captions and hashtag sets for small businesses."
    )
    parser.add_argument("--topic", required=True,
                        help="What the post is about, e.g. 'fresh sourdough'")
    parser.add_argument("--niche", default="general",
                        choices=sorted(HASHTAG_BANK.keys()),
                        help="Business niche (default: general)")
    parser.add_argument("--platform", default="instagram",
                        choices=sorted(PLATFORM_HASHTAG_LIMIT.keys()),
                        help="Target platform (default: instagram)")
    parser.add_argument("--count", type=int, default=1,
                        help="How many caption options to print (default: 1)")
    parser.add_argument("--seed", type=int, default=None,
                        help="Random seed, for repeatable output")
    args = parser.parse_args(argv)

    if args.count < 1:
        print("--count must be at least 1", file=sys.stderr)
        return 2

    rng = random.Random(args.seed)
    for i in range(args.count):
        if args.count > 1:
            print("--- Option {} ---".format(i + 1))
        print(build_caption(args.topic, args.niche, args.platform, rng))
        if i < args.count - 1:
            print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
