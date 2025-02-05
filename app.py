from flask import Flask, render_template, request, redirect, url_for
import openai
import os
from dotenv import load_dotenv
import pandas as pd
import requests
from moviepy.editor import VideoFileClip

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Retrieve the OpenAI API key from the .env file
openai.api_key = os.getenv('OPENAI_API_KEY')

# Example data structure to store processed videos
video_data = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global video_data
    
    if request.method == 'POST':
        video_links = request.form.get('video_links').split(',')
        
        for link in video_links:
            link = link.strip()
            transcript = generate_transcript(link)
            summary, stakeholders = generate_summary_and_stakeholders(transcript)
            
            video_data.append({
                'link': link,
                'summary': summary,
                'stakeholders': stakeholders,
                'transcript_link': url_for('view_transcript', link=link)
            })

        return redirect(url_for('index'))
    
    return render_template('index.html', videos=video_data)


@app.route('/transcript/<path:link>')
def view_transcript(link):
    transcript = generate_transcript(link)
    return render_template('transcript.html', transcript=transcript, link=link)


def generate_transcript(link, chunk_duration=300):
    response = requests.get(link)
    media_file_path = "/tmp/media_file"

    content_type = response.headers.get('Content-Type')
    if 'video' in content_type:
        media_file_path += '.mp4'
    elif 'audio' in content_type:
        media_file_path += '.mp3'
    else:
        return "Unsupported media type"

    with open(media_file_path, 'wb') as media_file:
        media_file.write(response.content)

    if media_file_path.endswith('.mp4'):
        video = VideoFileClip(media_file_path)
        audio_file_path = "/tmp/audio_file.mp3"
        video.audio.write_audiofile(audio_file_path)
        media_file_path = audio_file_path
    else:
        audio_file_path = media_file_path

    audio = VideoFileClip(audio_file_path).audio
    audio_duration = audio.duration

    transcripts = []
    start_time = 0

    while start_time < audio_duration:
        end_time = min(start_time + chunk_duration, audio_duration)
        chunk_path = f"/tmp/audio_chunk_{start_time}-{end_time}.mp3"
        
        audio.subclip(start_time, end_time).write_audiofile(chunk_path)
        
        try:
            transcript_response = openai.Audio.transcribe(
                model="whisper-1",
                file=open(chunk_path, "rb")
            )
            transcripts.append(transcript_response['text'])
        except Exception as e:
            transcripts.append(f"Error during transcription: {str(e)}")
        
        os.remove(chunk_path)
        
        start_time += chunk_duration

    combined_transcript = " ".join(transcripts)

    os.remove(media_file_path)
    if media_file_path.endswith('.mp4'):
        os.remove(audio_file_path)
    
    return combined_transcript


def generate_summary_and_stakeholders(transcript):
    summary_prompt = f"Summarize the following transcript: {transcript}"
    stakeholders_prompt = f"Identify key stakeholders from the following transcript: {transcript}"

    # Generate summary using the new API
    summary_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": summary_prompt}
        ]
    )
    summary = summary_response['choices'][0]['message']['content'].strip()

    # Identify stakeholders using the new API
    stakeholders_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": stakeholders_prompt}
        ]
    )
    stakeholders = stakeholders_response['choices'][0]['message']['content'].strip()

    return summary, stakeholders
if __name__ == '__main__':
    app.run(debug=True)
