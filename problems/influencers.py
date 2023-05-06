def get_num_verified_in_audience(influencer, count=0, influencers_counted={}):
    influencers_counted[influencer.name] = True
    print(count)
    for name, follower in influencer.followers.items():
        print(name)
        if influencers_counted.get(name, None):
            continue
        if follower.is_verified:
            count += 1
            print(count)
            count = get_num_verified_in_audience(follower, count, influencers_counted)
            print(count)
        influencers_counted[name] = True    
    return count


# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


class Influencer:
    def __init__(self, name, is_verified):
        self.name = name
        self.is_verified = is_verified
        self.followers = {}


def test(influencer):
    result = get_num_verified_in_audience(influencer)
    print(f"{influencer.name} has {result} verified followers in their audience")


def main():
    tiff = Influencer("Tiff", False)
    john = Influencer("John", False)
    amit = Influencer("Amit", True)
    jake = Influencer("Jake", False)
    dan = Influencer("Dan", False)
    steph = Influencer("Steph", True)
    jess = Influencer("Jess", True)
    jill = Influencer("Jill", False)
    mike = Influencer("Mike", False)
    courtland = Influencer("Courtland", True)

    tiff.followers = {
        john.name: john,
        amit.name: amit,
        jake.name: jake,
        dan.name: dan,
    }

    amit.followers = {
        steph.name: steph,
        jess.name: jess,
    }

    dan.followers = {
        tiff.name: tiff,
        jill.name: jill,
        mike.name: mike,
        courtland.name: courtland,
    }
    #test(tiff)
    test(amit)
    #test(dan)


main()
