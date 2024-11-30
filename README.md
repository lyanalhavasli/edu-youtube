# edu-youtube
## Dataset Description
YouTube Watch History
Source: Will be exported from personal YouTube watch history using Google Takeout.
Expected Contents:
Video Titles: Titles of all watched videos.
Timestamps: Dates and times when each video was watched.
Video URLs: Links to the watched videos.
Channel Information: Names of the channels from which videos were watched.
Video Descriptions: Additional metadata that may help categorize videos.
Project Plan and Methodology
## Data Collection
YouTube Data:
Use Google Takeout to export the YouTube watch history.
Academic Data:
Compile a list of courses and their respective midterm dates and subject areas.
## Data Preparation
Data Cleaning:
Remove irrelevant entries (e.g., non-academic YouTube videos).
Handle missing or inconsistent data.
Ensure all timestamps are in a consistent timezone (e.g., local time).
Data Transformation:
Convert timestamps to datetime objects.
Categorize YouTube videos as course-related or non-course-related using keyword matching, video descriptions, and metadata.
Keywords: Use course titles, subject areas, and relevant topics to identify related videos.
Annotate videos with the corresponding course subject if applicable.
## Data Integration
Align Datasets:
Map YouTube video timestamps to the sabnaci exam email announcements to identify if they fall within midterm seasons.
Create a unified timeline to visualize and analyze YouTube viewing activity relative to midterm dates.
