# # database/supabase_client.py
# from supabase import create_client
# import config
# from datetime import datetime

# # Initialize the client
# supabase = create_client(config.SUPABASE_URL, config.SUPABASE_API_KEY)

# # Insert Data
# # def insert_data(data):
# #     # Format the time properly
# #     if 'interval_time' in data and data['interval_time']:
# #         try:
# #             if len(data['interval_time']) == 5:
# #                 data['interval_time'] = f"{data['interval_time']}:00"
# #         except ValueError:
# #             print("❌ Invalid time format for 'interval_time'. Expected HH:MM or HH:MM:SS")

# #     print("✅ Data to insert:", data)
# #     response = supabase.table("data_entries").insert(data).execute()

# #     # 📝 Supabase API doesn't use status_code; use .error instead:
# #     if response.status_code == 201:
# #         print("✅ Data inserted successfully.")
# #         return {"message": "Data entry added successfully"}
# #     elif response.status_code == 200:
# #         print("✅ Data inserted successfully.")
# #         return {"message": "Data entry added successfully"}
# #     else:
# #         print("❌ Error from Supabase:", response.data)
# #         return {"error": response.data}
    
# # def insert_data(data):
# #     # Format the time properly
# #     if 'interval_time' in data and data['interval_time']:
# #         try:
# #             if len(data['interval_time']) == 5:
# #                 data['interval_time'] = f"{data['interval_time']}:00"
# #         except ValueError:
# #             print("❌ Invalid time format for 'interval_time'. Expected HH:MM or HH:MM:SS")

# #     print("✅ Data to insert:", data)
# #     response = supabase.table("data_entries").insert(data).execute()

# #     if response.error is None:
# #         print("✅ Data inserted successfully.")
# #         return {"message": "Data entry added successfully"}
# #     else:
# #         print("❌ Error from Supabase:", response.error)
# #         return {"error": str(response.error)}

# def insert_data(data):
#     # Make sure interval_time exists in the data dictionary
#     if 'interval_time' not in data:
#         data['interval_time'] = "00:00:00"
#         print("⚠️ 'interval_time' field missing. Setting default to '00:00:00'.")
#     # Handle empty or None values
#     elif data['interval_time'] is None or data['interval_time'] == "":
#         print("⚠️ 'interval_time' is empty. Setting default to '00:00:00'.")
#         data['interval_time'] = "00:00:00"  # Default to midnight if empty
#     else:
#         try:
#             # If time is in HH:MM format, convert it to HH:MM:SS
#             if len(data['interval_time']) == 5 and ":" in data['interval_time']:
#                 data['interval_time'] = f"{data['interval_time']}:00"
#                 print(f"✅ Formatted time from {data['interval_time'][0:5]} to: {data['interval_time']}")
            
#             # Validate time format
#             time_parts = data['interval_time'].split(':')
#             hours, minutes = int(time_parts[0]), int(time_parts[1])
            
#             # Basic validation of hours and minutes
#             if not (0 <= hours <= 23 and 0 <= minutes <= 59):
#                 print(f"⚠️ Invalid time values in: {data['interval_time']}. Setting to '00:00:00'")
#                 data['interval_time'] = "00:00:00"
#             elif len(time_parts) == 2:
#                 # If only HH:MM format (without seconds), add :00 for seconds
#                 data['interval_time'] = f"{data['interval_time']}:00"
#             elif len(time_parts) != 3:
#                 print(f"⚠️ Invalid time format: {data['interval_time']}. Setting to '00:00:00'")
#                 data['interval_time'] = "00:00:00"
#         except Exception as e:
#             print(f"❌ Error processing time format: {e}")
#             data['interval_time'] = "00:00:00"  # Fallback if any error occurs
    
#     # Log the final time being used
#     print(f"✅ Using interval_time: '{data['interval_time']}'")

#     # Ensure all float values are correctly formatted or set to 0.0 if empty
#     for key in [
#         'dust_weight', 'pyranometer_voltage', 'v_clean', 'i_clean',
#         'v_dusty', 'i_dusty', 'clean_panel_temp', 'dusty_panel_temp',
#         'ambient_shading_temp', 'ambient_surrounding_temp'
#     ]:
#         if key in data:
#             try:
#                 if data[key] == "" or data[key] is None:
#                     data[key] = 0.0
#                 else:
#                     data[key] = float(data[key])
#             except (ValueError, TypeError) as e:
#                 print(f"❌ Error converting {key} to float: {e}. Setting to 0.0")
#                 data[key] = 0.0

#     print("✅ Data to insert:", data)
    
#     # Execute the database insertion
#     try:
#         response = supabase.table("data_entries").insert(data).execute()
        
#         # Check for errors in response
#         if hasattr(response, 'error') and response.error is not None:
#             print(f"❌ Supabase error: {response.error}")
#             return {"error": str(response.error)}
#         else:
#             print("✅ Data inserted successfully.")
#             return {"message": "Data entry added successfully", "data": response.data}
#     except Exception as e:
#         print(f"❌ Exception during database insertion: {e}")
#         return {"error": str(e)}

# # Get All Data
# def get_all_data():
#     response = supabase.table("data_entries").select("*").execute()
    
#     if response.data:  # If data is present, it means fetching was successful
#         print("✅ Data fetched successfully.")
#         return response.data
#     elif response.error_message:  # Check for error message
#         print("❌ Error from Supabase:", response.error_message)
#         return {"error": response.error_message}
#     else:
#         print("❌ Unknown error occurred.")
#         return {"error": "Unknown error occurred"}