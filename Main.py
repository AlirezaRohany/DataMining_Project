import Read_Records
import Train
import Test

records = Read_Records.all_records
training_records = Train.training_records

print("\n")
print(records[53333].__dict__)

print("\n")

print("Total records:", len(records))
print("Training records:", len(training_records))
print("Cancelled training records:", len(Train.cancelled_training_records))
print("Not cancelled training records:", len(Train.not_cancelled_training_records))
print("Probability of cancellation in training data:", Train.P_is_cancelled_in_train)
print("Probability of not cancelling in training data:", Train.P_is_not_cancelled_in_train)


def print_statistics(sth, sth_cancel, sth_not_cancel, P_sth_cancel, P_sth_not_cancel):
    print("\n")
    print(sth, "distribution:")
    print("in cancelled:", len(sth_cancel), "    ", "in not cancelled", len(sth_not_cancel))
    print("in cancelled", "{:.2f}".format(P_sth_cancel * 100) + "%", "    ", "in not cancelled",
          "{:.2f}".format(P_sth_not_cancel * 100) + "%")


print_statistics("hotel", Test.hotel_cancel, Test.hotel_not_cancel, Test.P_hotel_cancel, Test.P_hotel_not_cancel)
print_statistics("is_repeated", Test.is_repeated_cancel, Test.is_repeated_not_cancel, Test.P_is_repeated_cancel,
                 Test.P_is_repeated_not_cancel)
print_statistics("reservation_status", Test.reservation_status_cancel, Test.reservation_status_not_cancel,
                 Test.P_reservation_status_cancel, Test.P_reservation_status_not_cancel)
print_statistics("meal", Test.meal_cancel, Test.meal_not_cancel, Test.P_meal_cancel, Test.P_meal_not_cancel)
print_statistics("reserved_room_type", Test.reserved_room_type_cancel, Test.reserved_room_type_not_cancel,
                 Test.P_reserved_room_type_cancel, Test.P_reserved_room_type_not_cancel)
print_statistics("customer_type", Test.customer_type_cancel, Test.customer_type_not_cancel, Test.P_customer_type_cancel,
                 Test.P_customer_type_not_cancel)
print_statistics("deposit_type", Test.deposit_type_cancel, Test.deposit_type_not_cancel, Test.P_deposit_type_cancel,
                 Test.P_deposit_type_not_cancel)
print_statistics("market_segment", Test.market_segment_cancel, Test.market_segment_not_cancel,
                 Test.P_market_segment_cancel, Test.P_market_segment_not_cancel)

print("\n")

print("The probability of cancellation of this booking:", "{:.6f}".format(Test.P_all_features_is_cancelled * 100) + "%")
print("The probability of not cancelling of this booking:",
      "{:.6f}".format(Test.P_all_features_is_not_cancelled * 100) + "%")

print(Test.answer)
print("\n")

print("True predictions:", Test.true_predictions)
print("False predictions:", Test.false_predictions)
print("Prediction quality:", Test.prediction_quality)
