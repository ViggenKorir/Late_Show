// {
// 	"info": {
// 		"_postman_id": "5682cab1-8868-4116-8315-fe678c14c97c",
// 		"name": "challenge-4-lateshow",
// 		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
// 	},
// 	"item": [
// 		{
// 			"name": "episodes",
// 			"request": {
// 				"method": "GET",
// 				"header": [],
// 				"url": {
// 					"raw": "http://localhost:5555/episodes",
// 					"protocol": "http",
// 					"host": [
// 						"localhost"
// 					],
// 					"port": "5555",
// 					"path": [
// 						"episodes"
// 					]
// 				}
// 			},
// 			"response": []
// 		},
// 		{
// 			"name": "guests",
// 			"request": {
// 				"method": "GET",
// 				"header": [],
// 				"url": {
// 					"raw": "http://localhost:5555/guests",
// 					"protocol": "http",
// 					"host": [
// 						"localhost"
// 					],
// 					"port": "5555",
// 					"path": [
// 						"guests"
// 					]
// 				}
// 			},
// 			"response": []
// 		},
// 		{
// 			"name": "episode/<int:id>",
// 			"request": {
// 				"method": "GET",
// 				"header": [],
// 				"url": {
// 					"raw": "http://localhost:5555/episodes/1",
// 					"protocol": "http",
// 					"host": [
// 						"localhost"
// 					],
// 					"port": "5555",
// 					"path": [
// 						"episodes",
// 						"1"
// 					]
// 				}
// 			},
// 			"response": []
// 		},
// 		{
// 			"name": "episodes/<int:id>",
// 			"request": {
// 				"method": "DELETE",
// 				"header": [],
// 				"url": {
// 					"raw": "http://localhost:5555/episodes/1",
// 					"protocol": "http",
// 					"host": [
// 						"localhost"
// 					],
// 					"port": "5555",
// 					"path": [
// 						"episodes",
// 						"1"
// 					]
// 				}
// 			},
// 			"response": []
// 		},
// 		{
// 			"name": "appearances",
// 			"request": {
// 				"method": "POST",
// 				"header": [],
// 				"body": {
// 					"mode": "raw",
// 					"raw": "{\n  \"rating\": 5,\n  \"episode_id\": 2,\n  \"guest_id\": 3\n}",
// 					"options": {
// 						"raw": {
// 							"language": "json"
// 						}
// 					}
// 				},
// 				"url": {
// 					"raw": "http://localhost:5555/appearances",
// 					"protocol": "http",
// 					"host": [
// 						"localhost"
// 					],
// 					"port": "5555",
// 					"path": [
// 						"appearances"
// 					]
// 				}
// 			},
// 			"response": []
// 		}
// 	]
// }