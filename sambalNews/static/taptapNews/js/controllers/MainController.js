 app.controller('MainController', ['$scope', function($scope) { 
  $scope.products = [
  	{ 
    	name: 'The Book of Trees',
    	pubdate: new Date('2014', '03', '08'), 
    	cover: 'img/the-book-of-trees.jpg',
        source:'iinnjaaa',
    	likes: 0,
        dislikes: 0,
    	comments : [{
			name: 'Hassan',
			text: 'Ajab khabare mozzzakhrafi'
		}]
  	}, 
  	{ 
    	name: 'Program or be Programmed', 
    	pubdate: new Date('2013', '08', '01'), 
    	cover: 'img/program-or-be-programmed.jpg',
        source:'iinnjaaa',
    	likes: 0 ,
        dislikes: 0,
    	comments : [{
			name: 'Hassan',
			text: 'Ajab khabare mozzzakhrafi'
		},{
			name: 'Pooriaye divaane',
			text: 'Salam doki'
		}]
  	}, 
  	{ 
    	name: 'Harry Potter & The Prisoner of Azkaban', 
        source:'iinnjaaa',
    	pubdate: new Date('1999', '07', '08'), 
    	cover: 'b4/Harry_Potter_and_the_Prisoner_of_Azkaban_(US_cover).jpg',
    	likes: 0,
        dislikes: 0,
  	}, 
  	{ 
    	name: 'Ready Player One', 
    	pubdate: new Date('2011', '08', '16'), 
    	cover: 'a4/Ready_Player_One_cover.jpg',
    	likes: 0,
        dislikes: 4
  	}
  ];
        $scope.plusOne = function(index) { 
            $scope.products[index].likes += 1; 
            };
        $scope.minusOne = function(index) { 
            $scope.products[index].dislikes += 1; 
            };
        $scope.sendComment=function(index){
            $scope.products[index].comments=[{
			name: 'HAAAAAAAJIIII',
			text:'asd'
		}];
        };
        
}]);
