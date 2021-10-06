from backoffice.models import Topic


def get_mailing_list(category_id):
    """This one is gonna be an ugly piece of code :
    For a category_id (topic_id but avoiding repetition)
    passed as argument, function will fetch
    all profiles subscribed to the Topic, then the matching
    users accounts, get their mail and return all the relevant emails
    in a distribution list. Yes that was a long docstring"""

    mailing_list = []
    topic = (Topic.objects.filter(pk=category_id))[0]
    profile_set = topic.subscriptions.all()

    for profile in profile_set:
        if len(profile.user.email) > 0:
            mailing_list.append(profile.user.email)

    return mailing_list
