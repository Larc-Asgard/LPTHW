from flask import Flask, session, request
from flask import url_for, redirect, render_template
import map


app = Flask(__name__)

@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:
        thescene = map.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene)
    else:
    # The user doesn't have a session...
    # What should your code do in response?
    # Does that mean the game hasn't launched?
        return render_template('you_died.html')

@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    if 'scene' in session:
        if userinput is None:
            # Weird, a POST request to /game with no user input... what should your code do?
            return render_template('show_scene_error.html')
        else:
            currentscene = map.SCENES[session['scene']]
            nextscene = currentscene.go(userinput)
            if nextscene is None:
            # There's no transition for that user input.
            # what should your code do in response?
            # this is written to pop out an error message
            # then I decide to use button design so it happen in different circumstances
            # it is when you hop around with broswer and has an input that is not correct when the session
            # as stated in the error message
                return render_template('show_scene_error.html', scene = currentscene)

            else:
                session['scene'] = nextscene.urlname
                return render_template('show_scene.html', scene = nextscene)
    else:
        # There's no session, how could the user get here?
        # What should your code do in response?
        # I think I should make a cheating.html
        return render_template('you_died.html')

# This URL initializes the session with starting values
@app.route('/')
def index():
    session['scene'] = map.START.urlname
    return redirect(url_for('game_get')) # redirect the browser to the url for game_get

app.secret_key = 'thebestsecretkeyisscretkey'

#boiler plate!
if __name__ == "__main__":
    app.run()
