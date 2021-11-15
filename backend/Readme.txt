------------------------/Admin Authentication Endpoints/---------------------
POST /api/admin/register
POST /api/admin/login
GET /api/admin/user
POST /api/admin/logout
PUT /api/admin/users/info
PUT /api/admin/users/password

------------------------/Admin Endpoints/---------------------
GET/POST /api/admin/products
GET/PUT/DELETE/ /api/admin/products/{product_id}
GET /api/admin/users/{user_id}/links
GET /api/admin/orders
GET /api/admin/ambassadors

------------------------/Ambassador Authentication Endpoints/---------------------
POST /api/ambassador/register
POST /api/ambassador/login
GET /api/ambassador/user
POST /api/ambassador/logout
PUT /api/ambassador/users/info
PUT /api/ambassador/users/password

------------------------/Ambassador Endpoints/---------------------
GET /api/ambassador/products/frontend
GET /api/ambassador/products/backend
POST /api/ambassador/links
GET /api/ambassador/stats
GET /api/ambassador/rankings

------------------------/Checkout Endpoints/---------------------
GET /api/checkout/links/{code}  #get all the data that we need in order to create an order.
POST /api/checkout/orders       #create the order (complete=false)
POST /api/checkout/orders/confirm #change the complete from 0 to 1


------------------------/Commands/---------------------
mng populate_ambassadors
mng update_rankings 

------------------------/docker commands/---------------------

sudo docker-compose exec redis sh
KEYS *

------------------------/Requirement/---------------------
yay -S mailhog-bin
mailhog #run mailhog


