BaseApp.controller("IndexCtrl", function($scope){
    //Executed on Controller load
    var index = this;
    index.blog_entries = [
        {
            "name": "Hello!",
            "timestamp": "A few seconds ago",
            "body": "Welcome to the Wanderers of Light, a FFXIV:ARR LS, and perhaps an FC in embryo.  Enjoy your stay!"
        },
        {
            "name": "Another Post For Good Measure",
            "timestamp": "Yesterday",
            "body": "Here's another post.  I need to see how multiple posts are rendered on the page",
        },
    ];
});
