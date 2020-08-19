import Hotel_Booking_Record
import csv

file_name = 'hotel_bookings.csv'


def read_csv_file(filename):
    records = [Hotel_Booking_Record.HBR() for i in range(119390)]
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                t = line_count - 1
                records[t].hotel = row[0]
                records[t].is_cancelled = row[1]
                records[t].lead_time = row[2]
                records[t].arrival_date_year = row[3]
                records[t].arrival_date_month = row[4]
                records[t].arrival_date_week_number = row[5]
                records[t].arrival_date_day_of_month = row[6]
                records[t].stays_in_weekend_nights = row[7]
                records[t].stays_in_week_nights = row[8]
                records[t].adults = row[9]
                records[t].children = row[10]
                records[t].babies = row[11]
                records[t].meal = row[12]
                records[t].country = row[13]
                records[t].market_segment = row[14]
                records[t].distribution_channel = row[15]
                records[t].is_repeated_guest = row[16]
                records[t].previous_cancellations = row[17]
                records[t].previous_bookings_not_canceled = row[18]
                records[t].reserved_room_type = row[19]
                records[t].assigned_room_type = row[20]
                records[t].booking_changes = row[21]
                records[t].deposit_type = row[22]
                records[t].agent = row[23]
                records[t].company = row[24]
                records[t].days_in_waiting_list = row[25]
                records[t].customer_type = row[26]
                records[t].adr = row[27]
                records[t].required_car_parking_spaces = row[28]
                records[t].total_of_special_requests = row[29]
                records[t].reservation_status = row[30]
                records[t].reservation_status_date = row[31]
                line_count += 1
    return records


all_records = read_csv_file(file_name)