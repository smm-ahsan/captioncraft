# CaptionCraft

A tiny, dependency-free command line tool that drafts social media captions
and hashtag sets for small businesses and solo marketers.

Give it a topic, a business niche and a platform, and it prints ready to post
caption options: a hook, a short body, a platform-aware call to action, and a
hashtag set sized for that platform.

## Why

Small businesses post every day but rarely have a copywriter. CaptionCraft
covers the blank-page moment: it gives you a solid first draft in one second,
which you then personalise before posting.

## Features

- Zero dependencies - pure Python 3 standard library
- Niches: cafe, restaurant, bakery, salon, gym, realestate, general
- Platforms: instagram, facebook, linkedin, tiktok
- Hashtag count adapts to each platform's norms
- Multiple caption options per run, optional seed for repeatable output

## Install

No installation needed. Clone the repo and run it with Python 3:

```bash
git clone https://github.com/smmahsan/captioncraft.git
cd captioncraft
python3 captioncraft.py --help
```

## Usage

```bash
python3 captioncraft.py --topic "fresh sourdough" --niche bakery --platform instagram
python3 captioncraft.py --topic "new brunch menu" --niche cafe --platform facebook --count 3
python3 captioncraft.py --topic "summer hair packages" --niche salon --platform tiktok --seed 7
```

Sample output:

```
Stop scrolling. fresh sourdough just landed.

Small batch, big flavour, zero shortcuts. That is how we do things here.

Save this post and tag a friend who would love it.

#BakersOfInstagram #BakeryLife #SupportLocal #FreshFromTheOven ...
```

See [examples.md](examples.md) for full sample runs.

## Roadmap

- More niches (clinics, car services, tutors, photographers)
- Tone switch: playful, premium, urgent
- Read custom hashtag banks from a JSON file

## Contributing

Issues and pull requests are welcome. If you run a small business and a niche
or hashtag bank is missing, open an issue with your business type and the
hashtags you actually use.

## License

MIT - see [LICENSE](LICENSE).
