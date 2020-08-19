import Read_Records
import Train

answer = 0
true_predictions = 0
false_predictions = 0


def check_some_features(recs, sth, str):
    sth_cancel_or_not = []
    for rec in recs:
        if getattr(rec, str) == sth:
            sth_cancel_or_not.append(rec)
    return sth_cancel_or_not


for i in range(len(Read_Records.all_records)):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 211 == 0:
        # testing a record
        new_record = Read_Records.all_records[i]

        # hotel, is_repeated, reservation_status, agent, company, meal, reserved_room_type, customer_type, country, deposit_type, market_segment:
        hotel = new_record.hotel
        is_repeated = new_record.is_repeated_guest
        reservation_status = new_record.reservation_status
        meal = new_record.meal
        reserved_room_type = new_record.reserved_room_type
        customer_type = new_record.customer_type
        deposit_type = new_record.deposit_type
        market_segment = new_record.market_segment

        hotel_cancel = check_some_features(Train.cancelled_training_records, hotel, "hotel")
        is_repeated_cancel = check_some_features(Train.cancelled_training_records, is_repeated, "is_repeated_guest")
        reservation_status_cancel = check_some_features(Train.cancelled_training_records, reservation_status,
                                                        "reservation_status")
        meal_cancel = check_some_features(Train.cancelled_training_records, meal, "meal")
        reserved_room_type_cancel = check_some_features(Train.cancelled_training_records, reserved_room_type,
                                                        "reserved_room_type")
        customer_type_cancel = check_some_features(Train.cancelled_training_records, customer_type, "customer_type")
        deposit_type_cancel = check_some_features(Train.cancelled_training_records, deposit_type, "deposit_type")
        market_segment_cancel = check_some_features(Train.cancelled_training_records, market_segment, "market_segment")

        hotel_not_cancel = check_some_features(Train.not_cancelled_training_records, hotel, "hotel")
        is_repeated_not_cancel = check_some_features(Train.not_cancelled_training_records, is_repeated,
                                                     "is_repeated_guest")
        reservation_status_not_cancel = check_some_features(Train.not_cancelled_training_records, reservation_status,
                                                            "reservation_status")
        meal_not_cancel = check_some_features(Train.not_cancelled_training_records, meal, "meal")
        reserved_room_type_not_cancel = check_some_features(Train.not_cancelled_training_records, reserved_room_type,
                                                            "reserved_room_type")
        customer_type_not_cancel = check_some_features(Train.not_cancelled_training_records, customer_type,
                                                       "customer_type")
        deposit_type_not_cancel = check_some_features(Train.not_cancelled_training_records, deposit_type,
                                                      "deposit_type")
        market_segment_not_cancel = check_some_features(Train.not_cancelled_training_records, market_segment,
                                                        "market_segment")

        # hotel:good (2types)
        P_hotel_cancel = len(hotel_cancel) / len(Train.cancelled_training_records)  # 2/9
        P_hotel_not_cancel = len(hotel_not_cancel) / len(Train.not_cancelled_training_records)  # 3/5

        # is_repeated_guest: good (2types)
        P_is_repeated_cancel = len(is_repeated_cancel) / len(Train.cancelled_training_records)
        P_is_repeated_not_cancel = len(is_repeated_not_cancel) / len(Train.not_cancelled_training_records)

        # reservation_status: very bad feature since its basically the target variable, we ignore it. (3types)
        P_reservation_status_cancel = len(reservation_status_cancel) / len(Train.cancelled_training_records)
        P_reservation_status_not_cancel = len(reservation_status_not_cancel) / len(Train.not_cancelled_training_records)

        # agent and company: 13% of agent ID and 94% of company ID is missing; so we ignore both of them.

        # meal: ordinary (5types)
        P_meal_cancel = len(meal_cancel) / len(Train.cancelled_training_records)
        P_meal_not_cancel = len(meal_not_cancel) / len(Train.not_cancelled_training_records)

        # reserved_room_type: ordinary (10types)
        P_reserved_room_type_cancel = len(reserved_room_type_cancel) / len(Train.cancelled_training_records)
        P_reserved_room_type_not_cancel = len(reserved_room_type_not_cancel) / len(Train.not_cancelled_training_records)

        # customer_type: good (4types)
        P_customer_type_cancel = len(customer_type_cancel) / len(Train.cancelled_training_records)
        P_customer_type_not_cancel = len(customer_type_not_cancel) / len(Train.not_cancelled_training_records)

        # country: there are too many countries and it means nothing to our prediction. We will ignore this feature

        # deposit_type: ordinary (3types)
        P_deposit_type_cancel = len(deposit_type_cancel) / len(Train.cancelled_training_records)
        P_deposit_type_not_cancel = len(deposit_type_not_cancel) / len(Train.not_cancelled_training_records)

        # market_segment:ordinary  (8types)
        P_market_segment_cancel = len(market_segment_cancel) / len(Train.cancelled_training_records)
        P_market_segment_not_cancel = len(market_segment_not_cancel) / len(Train.not_cancelled_training_records)

        # all features
        P_all_features_is_cancelled = P_hotel_cancel * P_is_repeated_cancel * P_meal_cancel * P_reserved_room_type_cancel * P_customer_type_cancel * P_deposit_type_cancel * P_market_segment_cancel * Train.P_is_cancelled_in_train
        P_all_features_is_not_cancelled = P_hotel_not_cancel * P_is_repeated_not_cancel * P_meal_not_cancel * P_reserved_room_type_not_cancel * P_customer_type_not_cancel * P_deposit_type_not_cancel * P_market_segment_not_cancel * Train.P_is_not_cancelled_in_train

        if P_all_features_is_cancelled > P_all_features_is_not_cancelled:
            # answer = "this booking will be cancelled"
            if int(new_record.is_cancelled) == 1:
                true_predictions += 1
            else:
                false_predictions += 1
        elif P_all_features_is_cancelled < P_all_features_is_not_cancelled:
            # answer = "this booking will not be cancelled"
            if int(new_record.is_cancelled) == 0:
                true_predictions += 1
            else:
                false_predictions += 1

prediction_quality = true_predictions / (true_predictions + false_predictions)
