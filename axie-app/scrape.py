# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 01:01:59 2021

@author: Charles
"""

from flask import Blueprint, request, render_template, g, redirect, url_for

from wrapper import get_axie_market_list

bp = Blueprint('scrape',
               __name__,
               # url_prefix='/auth'
               )

@bp.route('/scrape', methods=(['GET', 'POST']))
def scrape():
    # if you would like to search...
    if request.method == 'POST':  
        # these are the fields you can fill in...
        parts = request.form['parts']
        classes = request.form['classes']
        pureness = request.form['pureness']
        breed_count = request.form['breed_count']
        hp = request.form['hp']
        skill = request.form['skill']
        speed = request.form['speed']
        morale = request.form['morale']
        
        response = get_axie_market_list(
            parts = list(parts)
        )
        
        g.searched = True
        g.results = response
        
        return redirect(url_for('scrape.results'))
    
    return render_template('scrape.html')

@bp.route('/results', methods=(['GET', 'POST']))
def results():
    # if you would like to search...
    if request.method == 'POST':  
        # these are the fields you can fill in...
        parts = request.form['parts']
        classes = request.form['classes']
        pureness = request.form['pureness']
        breed_count = request.form['breed_count']
        hp = request.form['hp']
        skill = request.form['skill']
        speed = request.form['speed']
        morale = request.form['morale']
        
        response = get_axie_market_list(
            parts = list(parts)
        )
        
        g.results = response
        
        return redirect(url_for('scrape.results'))
    
    return render_template('results.html')