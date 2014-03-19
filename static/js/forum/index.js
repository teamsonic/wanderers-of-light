BaseApp.controller("ForumIndexCtrl", function($scope){
    //Executed on controller load
    var forum_idx = this;
    this.boards = [
        {
            'name': 'General',
            'description': "Talk about anything and everything, whether it's related to FFXIV or not",
            'topics': '5',
            'messages': '40',
            'last_post': 'Yesterday 3:32 AM',
        },
        {
            'name': 'The Binding Coil of Bahamut',
            'description': "Talk shop about FFXIV's most-difficult raid yet",
            'topics': '5',
            'messages': '40',
            'last_post': 'Yesterday 3:32 AM',
        },
    ];
});
