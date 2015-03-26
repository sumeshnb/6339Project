/*
Author : Sumesh N Balan

File to fetch data asynchronously from backend

*/
var myApp = angular.module('moviebuzz', []);
myApp.controller('mbController', function($scope, $http) {

	$scope.movieDetails = function(item, event) {

		$scope.moviename1 = 'something1';
		$scope.$http = $http;

		//create 4 ajax requests
		//1. movie1
		//2. movie2
		//3. twitter statistics of movie1
		//4. twitter statistics fo movie2
		var responsePromise = $http.get('/moviedetails/');
		responsePromise.success(function(data, status, headers, config) {
			$scope.movieDetails = {};
			$scope.movieDetails = data;
		});
		responsePromise.error(function(data, status, headers, config) {
			alert("AJAX failed!");
		});
	};

});