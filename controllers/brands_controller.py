import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.brand import Brand
from models.item import Item
import repositories.item_repository as item_repo
import repositories.brand_repository as brand_repo

brands_blueprint = Blueprint("brands", __name__)

@brands_blueprint.route("/brands")
def brands():
    brands = brand_repo.select_all()
    return render_template("brands/index.html", all_brands = brands)

# NEW
# GET '/brands/new'
@brands_blueprint.route("/brands/new", methods=['GET'])
def new_brands():
    brands = brand_repo.select_all()
    status = brand_repo.select(id)
    return render_template("brands/new.html", status = status, all_brands = brands)

# CREATE
# POST '/brands'
@brands_blueprint.route("/brands",  methods=['POST'])
def create_item():
    print(request.form)
    name = request.form['name']
    status  = request.form['status']
    brand = Brand(name, status)
    brand_repo.save(brand)
    return redirect('/brands')


# SHOW
# GET '/brands/<id>'
@brands_blueprint.route("/brands/<id>", methods=['GET'])
def show_brand(id):
    brand = brand_repo.select(id)
    return render_template('brands/show.html', brand = brand)

# EDIT
# GET '/brands/<id>/edit'
@brands_blueprint.route("/brands/<id>/edit", methods=['GET'])
def edit_brand(id):
    brand = brand_repo.select(id)
    brands = brand_repo.select_all()
    return render_template('brands/edit.html', brand = brand, all_brands = brands)

# UPDATE
# PUT '/brands/<id>'
@brands_blueprint.route("/brands/<id>", methods=['POST'])
def update_brand(id):
    name = request.form['name']
    status  = request.form['status']
    brand = Brand(name, status)
    brand_repo.update(brand)
    return redirect('/brands')

# DELETE
# DELETE '/brands/<id>'
@brands_blueprint.route("/brands/<id>/delete", methods=['POST'])
def delete_brand(id):
    brand_repo.delete(id)
    return redirect('/brands')