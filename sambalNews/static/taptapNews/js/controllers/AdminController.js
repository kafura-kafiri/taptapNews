 
 app.controller('AdminController', ['$scope','$http', function($scope,$http) {
        $scope.addNews = function(title,source,category,tags,summary,text) {
              var f = document.getElementById('file').files[0],
                r = new FileReader();
                 r.onloadend = function(e){
                     var fileData = e.target.result;
                     var data = $.param(
                                         {
                                     data: {
                                              title:title,
                                         source:source,
                                         category: category,
                                         tags:tags,
                                         summary:summary,
                                         text:text,
                                         img:fileData
                                         }
                                          }
                       );
                                 var config = {headers : {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'}};
                     $http.post('/sambalNews/create_news', data, config)
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
                 r.readAsBinaryString(f);
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
