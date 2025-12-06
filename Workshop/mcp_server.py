import os
import django
from mcp.server.fastmcp import FastMCP
from asgiref.sync import sync_to_async
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Workshop.settings")
django.setup()
from ConferenceApp.models import Conference
from SessionApp.models import Session



mcp = FastMCP("conference_assistant")


@mcp.tool()
@sync_to_async
def list_conferences():
    """
    Return all conferences with their basic information.
    """
    conferences = Conference.objects.all().values(
        "conference_id", "name", "theme", "start_date", "end_date"
    )
    return list(conferences)



@mcp.tool()
@sync_to_async
def get_conference_by_id(conference_id: int):
    """
    Retrieve full details of a conference by ID.
    """
    try:
        conf = Conference.objects.get(conference_id=conference_id)
        return {
            "conference_id": conf.conference_id,
            "name": conf.name,
            "description": conf.description,
            "theme": conf.theme,
            "start_date": str(conf.start_date),
            "end_date": str(conf.end_date),
        }
    except Conference.DoesNotExist:
        return {"error": f"Conference {conference_id} not found."}



@mcp.tool()
@sync_to_async
def get_sessions_by_conference(conference_id: int):
    """
    Retrieve all sessions belonging to a specific conference.
    """
    sessions = Session.objects.filter(conference_id=conference_id).values(
        "session_id",
        "title",
        "topic",
        "session_day",
        "start_time",
        "end_time",
        "room",
    )
    return list(sessions)



@mcp.tool()
@sync_to_async
def conference_stats():
    """
    Return high-level statistical data about conferences & sessions.
    """
    total_conferences = Conference.objects.count()
    total_sessions = Session.objects.count()

    return {
        "total_conferences": total_conferences,
        "total_sessions": total_sessions,
    }



if __name__ == "__main__":
    mcp.run(transport="stdio")
