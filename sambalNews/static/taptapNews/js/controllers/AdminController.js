 
 app.controller('AdminController', ['$scope','$http', function($scope,$http) {
        $scope.sendNews = function(id,title,date,image,source,tags,breif) {
            alert(source);
            };
        $scope.sendTagInfo = function(name,oldname,del) {
            alert(del);
            };
        $scope.block = function(username) {
            alert(username);
            };
     $scope.addHashtag = function(hashtag) {
                       var data = $.param(
                {
                    data: {
                        tag: hashtag
                    }
                }
            );

            var config = {
                headers : {
                    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
                }
            };
         console.log(data)
              $http.post('/sambalNews/add_hashtag', data, config)
                .success(function (data, status, headers, config) {
                    $scope.ResponseDetails = data;
            })
            .error(function (data, status, header, config) {
                $scope.ResponseDetails = "Data: " + data +
                    "<hr />status: " + status +
                    "<hr />headers: " + header +
                    "<hr />config: " + config;
            });
            };
        }
]);
