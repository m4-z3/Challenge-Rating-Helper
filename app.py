from flask import Flask, render_template, flash, request
from joblib import load

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == "GET":
        return render_template('form.html')
    else:
        size = int(request.form['size'])
        ac = int(request.form['ac'])
        hp = int(request.form['hp'])
        strength = int(request.form['str'])
        dexterity = int(request.form['dex'])
        constitution = int(request.form['con'])
        intelligence = int(request.form['int'])
        wisdom = int(request.form['wis'])
        charisma = int(request.form['cha'])
        vulnerabilities = int(request.form['vulnerabilities'])
        resistance = int(request.form['resistances'])
        immunities = int(request.form['immunities'])
        conditions = int(request.form['conditions'])
        legendary_resistance = int(request.form['legendary_resistance'])
        actions_total = int(request.form['actions_total'])
        reactions = int(request.form['reactions'])
        legendary_actions_num = int(request.form['legendary_actions_num'])
        saving_throw_str =  1 if 'saving_throw_str' in request.form else 0
        saving_throw_dex = 1 if 'saving_throw_dex' in request.form else 0
        saving_throw_con = 1 if 'saving_throw_con' in request.form else 0
        saving_throw_int = 1 if 'saving_throw_int' in request.form else 0
        saving_throw_wis = 1 if 'saving_throw_wis' in request.form else 0
        saving_throw_cha = 1 if 'saving_throw_cha' in request.form else 0
        skill_athletics = 1 if 'skill_athletics' in request.form else 0
        skill_acrobatics = 1 if 'skill_acrobatics' in request.form else 0
        skill_sleight_of_hand = 1 if 'skill_sleight_of_hand' in request.form else 0
        skill_stealth = 1 if 'skill_stealth' in request.form else 0
        skill_arcana = 1 if 'skill_arcana' in request.form else 0
        skill_history = 1 if 'skill_history' in request.form else 0
        skill_investigation = 1 if 'skill_investigation' in request.form else 0
        skill_nature = 1 if 'skill_nature' in request.form else 0
        skill_religion = 1 if 'skill_religion' in request.form else 0
        skill_animal_handling = 1 if 'skill_animal_handling' in request.form else 0
        skill_insight = 1 if 'skill_insight' in request.form else 0
        skill_medicine = 1 if 'skill_medicine' in request.form else 0
        skill_perception = 1 if 'skill_perception' in request.form else 0
        skill_survival = 1 if 'skill_survival' in request.form else 0
        skill_deception = 1 if 'skill_deception' in request.form else 0
        skill_intimidation = 1 if 'skill_intimidation' in request.form else 0
        skill_performance = 1 if 'skill_performance' in request.form else 0
        skill_persuasion = 1 if 'skill_persuasion' in request.form else 0
        passive_perception = int(request.form['passive_perception'])
        blindsight = int(request.form['blindsight'])
        darkvision = int(request.form['darkvision'])
        tremorsense = int(request.form['tremorsense'])
        truesight = int(request.form['truesight'])
        speed = int(request.form['speed']) + int(request.form['burrow_speed']) + int(request.form['climb_speed']) + int(request.form['fly_speed']) + int(request.form['swim_speed'])
        has_walk = 1 if int(request.form['speed']) > 0 else 0
        has_burrow = 1 if int(request.form['burrow_speed']) > 0 else 0
        has_climb = 1 if int(request.form['climb_speed']) > 0 else 0
        has_fly = 1 if int(request.form['fly_speed']) > 0 else 0
        has_swim = 1 if int(request.form['swim_speed']) > 0 else 0
        legendary_actions_cost_1 = int(request.form['legendary_actions_cost_1'])
        legendary_actions_cost_2 = int(request.form['legendary_actions_cost_2'])
        legendary_actions_cost_3 = int(request.form['legendary_actions_cost_3'])
        actions_attack = int(request.form['actions_attack'])
        actions_avg_dmg = int(request.form['actions_avg_dmg'])
        data = [[size, ac, hp, strength, dexterity, constitution, intelligence, wisdom, charisma, vulnerabilities, resistance, immunities, conditions, legendary_resistance, actions_total, reactions, legendary_actions_num, saving_throw_str, saving_throw_dex, saving_throw_con, saving_throw_int, saving_throw_wis, saving_throw_cha, skill_athletics, skill_acrobatics, skill_sleight_of_hand, skill_stealth, skill_arcana, skill_history, skill_investigation, skill_nature, skill_religion, skill_animal_handling, skill_insight, skill_medicine, skill_perception, skill_survival, skill_deception, skill_intimidation, skill_performance, skill_persuasion, passive_perception, blindsight, darkvision, tremorsense, truesight, speed, has_walk, has_burrow, has_climb, has_fly, has_swim, legendary_actions_cost_1, legendary_actions_cost_2, legendary_actions_cost_3, actions_attack, actions_avg_dmg]]

        clf = load('model.joblib')
        challenge_rating = clf.predict(data)
        print(challenge_rating)
        return render_template('form.html', challenge_rating=challenge_rating[0])



if __name__ == "__main__":
    app.run(debug=True)